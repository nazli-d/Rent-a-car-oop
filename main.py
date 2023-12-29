import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
import sqlite3
import datetime
from abc import ABC, abstractmethod
import csv

class Araba(ABC):
    def __init__(self, marka, model, yil):
        self.id = None
        self.marka = marka
        self.model = model
        self._yil = yil  # Protected özellik
        self.__kilometre = 0  # Private özellik

    def get_yil(self):
        return self._yil

    def set_kilometre(self, km):
        if km >= 0:
            self.__kilometre = km
        else:
            print("Geçersiz kilometre değeri.")

    def get_kilometre(self):
        return self.__kilometre

    @abstractmethod
    def bakim(self):
        pass

class ElektrikliAraba(Araba):
    def __init__(self, marka, model, yil, batarya_durumu):
        super().__init__(marka, model, yil)
        self.batarya_durumu = batarya_durumu

    def bakim(self):
        return f"{self.marka} {self.model} elektrikli araba bakımı: Pil sağlığı kontrol ediliyor. Batarya Durumu: {self.batarya_durumu}. Kilometre: {self.get_kilometre()}"

class BenzinliAraba(Araba):
    def __init__(self, marka, model, yil, yakit_durumu):
        super().__init__(marka, model, yil)
        self.yakit_durumu = yakit_durumu

    def bakim(self):
        return f"{self.marka} {self.model} benzinli araba bakımı: Yağ değiştiriliyor. Yakıt Durumu: {self.yakit_durumu}. Kilometre: {self.get_kilometre()}"
class Kiralama:
    def __init__(self, musteri, araba, kiralama_tipi, sure):
        self.musteri = musteri
        self.araba = araba
        self.kiralama_tipi = kiralama_tipi
        self.sure = sure

    def hesapla_ucret(self):
        if self.kiralama_tipi == "günlük":
            return self.sure * 1000
        elif self.kiralama_tipi == "saatlik":
            return self.sure * 500
        else:
            print("Geçersiz kiralama tipi")
            return -1

class AracKiralamaUygulamasi:
    def __init__(self, root):
        self.root = root
        self.root.title("Araç Kiralama Uygulaması")

        self.create_database_connection()

        self.create_main_frame()

    def create_database_connection(self):
        # SQLite veritabanına bağlantı oluşturur
        self.baglanti = sqlite3.connect("rent-a.db")
        self.cursor = self.baglanti.cursor()

    def create_main_frame(self):
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.label_welcome = ttk.Label(self.main_frame, text="Araç Kiralama Uygulamasına Hoş Geldiniz!", font=('Arial', 16, 'bold', "italic"))
        self.label_welcome.grid(row=0, column=0, columnspan=3, pady=20)

        self.label_instruction = ttk.Label(self.main_frame, text="Adınız Soyadınız:", font=('Arial', 12))
        self.label_instruction.grid(row=1, column=0, columnspan=3, pady=10)

        self.entry_ad_soyad = ttk.Entry(self.main_frame, font=('Arial', 12))
        self.entry_ad_soyad.grid(row=2, column=0, columnspan=3, pady=10)

        # Giriş yap butonu ve stili
        self.button_giris = tk.Button(self.main_frame, text="Giriş Yap", command=self.musteri_giris,
                                      width=10, height=1, bg="purple", fg="white", font=("Arial", 12))
        self.button_giris.grid(row=3, column=0, columnspan=3, pady=20)

        self.button_export = ttk.Button(self.main_frame, text="Tabloyu Dışa Aktar", command=self.export_goster)
        self.button_export.grid(row=4, column=0, columnspan=3, pady=10)

    def musteri_giris(self):
        # Kullanıcının adını soyadını al
        ad_soyad = self.entry_ad_soyad.get()

        # Ad soyadın boş olup olmadığını kontrol et
        if not ad_soyad:
            messagebox.showwarning("Uyarı", "Lütfen adınızı ve soyadınızı girin.")
            return

        # Kullanıcı veritabanında ekli mi kontrol et
        musteri_id = self.musteri_varmi(ad_soyad)

        if musteri_id:
            self.musteri_id = musteri_id
            self.label_welcome.config(text=f"Hoş Geldin, {ad_soyad}!")
            self.label_instruction.grid_remove()
            self.entry_ad_soyad.grid_remove()
            self.button_giris.grid_remove()

            # Giriş yapıldıktan sonra araç listesini göster
            self.arac_listesi()

            # Giriş yapıldıktan sonra tabloyu dışa aktar butonunu gizle
            self.button_export.grid_remove()
        else:
            messagebox.showwarning("Uyarı", "Kayıtlı bir müşteri bulunamadı. Lütfen kayıtlı müşteri adını girin.")

    def musteri_varmi(self, ad_soyad):
        self.cursor.execute("SELECT id FROM musteri WHERE ad_soyad = ?", (ad_soyad,))
        musteri = self.cursor.fetchone()

        if musteri:
            return musteri[0]
        else:
            return None

    def arac_listesi(self):
        araclar = self.get_arac_list()

        # Treeview (tablo) oluştur
        self.tree_araclar = ttk.Treeview(self.main_frame, columns=("id", "Marka", "Model", "Yıl", "Tip", "Durum"), show="headings")
        self.tree_araclar.heading("id", text="id")
        self.tree_araclar.heading("Marka", text="Marka")
        self.tree_araclar.heading("Model", text="Model")
        self.tree_araclar.heading("Yıl", text="Yıl")
        self.tree_araclar.heading("Tip", text="Tip")
        self.tree_araclar.heading("Durum", text="Durum")

        # Araçları tabloya ekle
        for arac in araclar:
            self.tree_araclar.insert("", "end", values=arac)

        # Tabloyu göster
        self.tree_araclar.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E))

        self.button_kirala = ttk.Button(self.main_frame, text="Araç Kirala", command=self.arac_kirala)
        self.button_kirala.grid(row=2, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

    def get_arac_list(self):
        self.cursor.execute(
            "SELECT arabalar.id, marka, model, yil, tip, durumu FROM arabalar WHERE durumu IN ('müsait', 'kiralandı')")
        return self.cursor.fetchall()

    def arac_kirala(self):
        # Seçilen aracı al
        selected_item = self.tree_araclar.selection()

        if selected_item:
            arac_id = self.tree_araclar.item(selected_item, "values")[0]
            arac_durumu = self.tree_araclar.item(selected_item, "values")[5]
            # Eğer araç zaten kiralandıysa uyarı ver
            if arac_durumu == 'kiralandı':
                messagebox.showwarning("Uyarı", "Bu araç zaten kiralanmış!")
                return
            # Kiralama tipi ve süreyi al
            kiralama_tipi, sure = self.show_kiralama_dialog()

            if kiralama_tipi and sure:
                arac = self.get_arac_id(arac_id)

                # Aracın bakım durumu GUI'de gösteriliyor
                self.show_arac_bakim_durumu(arac)

                # Aracın durumunu güncelle
                self.arac_durumu_guncelle(arac_id)

                # Kiralama bilgilerini veritabanına ekle
                kiralama = Kiralama(self.musteri_id, arac, kiralama_tipi, sure)
                self.add_kiralama_bilgisi(kiralama)

                # Ücreti hesapla ve kullanıcıya göster
                ucret = kiralama.hesapla_ucret()
                if ucret != -1:
                    messagebox.showinfo("Başarılı", f"Araç kiralandı! Ücret: {ucret} TL")
                    self.root.destroy()

    def export_goster(self):
        table_name = simpledialog.askstring("Tablo Seçimi", "Dışa aktarmak istediğiniz tabloyu girin: (arabalar/musteri/kiralama)")
        if table_name:
            self.export_to_csv(table_name)

    def export_to_csv(self, table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        table_data = self.cursor.fetchall()

        if table_data:
            with open(f"{table_name}.csv", mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([i[0] for i in self.cursor.description])  # Sütun başlıklarını yaz
                writer.writerows(table_data)  # Verileri yaz
            messagebox.showinfo("Başarılı", f"{table_name} tablosu dışa aktarıldı!")
        else:
            messagebox.showwarning("Uyarı", f"{table_name} tablosunda veri bulunamadı.")


    def arac_durumu_guncelle(self, arac_id):
        self.cursor.execute("UPDATE arabalar SET durumu = 'kiralandı' WHERE id = ?", (arac_id,))
        self.baglanti.commit()

    def add_kiralama_bilgisi(self, kiralama):
        ucret = kiralama.hesapla_ucret()  # Calculate the rental fee

        self.cursor.execute(
            "INSERT INTO kiralama (musteri_id, araba_id, kiralama_tipi, sure, ucret, durumu) VALUES ( ?, ?, ?, ?, ?, ?)",
            (kiralama.musteri, kiralama.araba.id, kiralama.kiralama_tipi, kiralama.sure, ucret, 'kiralandı'))
        self.baglanti.commit()

    def show_arac_bakim_durumu(self, arac):
        bakim_durumu = arac.bakim()
        messagebox.showinfo("Bakım Durumu", bakim_durumu)


    def show_kiralama_dialog(self):
        dialog = tk.Toplevel(self.root)

        ttk.Label(dialog, text="Kiralama Tipi:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        kiralama_tipi_var = tk.StringVar()
        ttk.Combobox(dialog, textvariable=kiralama_tipi_var, values=["günlük", "saatlik"]).grid(row=0, column=1,
                                                                                                padx=10, pady=10,
                                                                                                sticky=tk.W)

        ttk.Label(dialog, text="Kiralama Süresi:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
        sure_var = tk.IntVar()
        ttk.Entry(dialog, textvariable=sure_var).grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        ttk.Button(dialog, text="Tamam", command=dialog.destroy).grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        dialog.wait_window()

        return kiralama_tipi_var.get(), sure_var.get()
    def get_arac_id(self, arac_id):
        self.cursor.execute("SELECT * FROM arabalar WHERE id = ?", (arac_id,))
        arac_data = self.cursor.fetchone()

        if arac_data:
            arac_id, marka, model, yil, tip, durumu, kilometre = arac_data  # Unpack the values
            if tip == 'Elektrikli':
                elektrikli_arac = ElektrikliAraba(marka, model, yil, batarya_durumu="Yüksek")
                elektrikli_arac.id = arac_id
                elektrikli_arac.set_kilometre(kilometre)
                return elektrikli_arac
            elif tip == 'Benzinli':
                benzinli_arac = BenzinliAraba(marka, model, yil, yakit_durumu="Doluluk Oranı: %100")
                benzinli_arac.id = arac_id
                benzinli_arac.set_kilometre(kilometre)
                return benzinli_arac
        else:
            return None


if __name__ == "__main__":
    root = tk.Tk()
    app = AracKiralamaUygulamasi(root)
    root.mainloop()
