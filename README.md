
# Araç Kiralama Uygulaması (Rent Car OOP GUI)

Araba kiralama uygulaması, Python programlama dili kullanılarak geliştirilen ve grafik kullanıcı arayüzü (GUI) tasarımını bir araya getirerek, araç kiralama süreçlerini yönetebilen bir yazılımın nasıl oluşturulacağını gösterir. Kodun temelinde, nesne tabanlı programlama (OOP) prensipleri ve SQLite veritabanı kullanımı bulunmaktadır.

![image](https://github.com/nazli-d/Rent-a-car-oop/assets/96622076/30e22775-b526-49de-b463-9b540d82bc8d)

## Özellikler

- **Müşteri Girişi**: Kullanıcıların adlarını girerek sisteme giriş yapmalarını sağlar.
- **Araç Listesi**: Kullanıcıların kiralayabileceği arabaların listesini görüntüler.
- **Araç Kiralama**: Müşterilerin seçtikleri araçları belirli bir süre için kiralayabilmelerini sağlar.
- **Veritabanı Entegrasyonu**: SQLite veritabanı üzerinde müşteri, araç ve kiralama bilgilerini saklar.
- **Tablo Dışa Aktarma**: Veritabanındaki bilgileri CSV formatında dışa aktarma (export) imkanı sunar.

## Nasıl Kullanılır?

1. **Müşteri Girişi**: Adınızı soyadınızı girin ve "Giriş Yap" butonuna tıklayarak sisteme giriş yapın.
2. **Araç Seçimi**: Müsait araç listesinden istediğiniz aracı seçin ve kiralama tipi ile süreyi belirleyin.
3. **Kiralama İşlemi**: Kiralama işlemini onaylayın ve aracınızı kiralayın. Aracın bakım durumu da gösterilecektir.
4. **Veritabanı Dışa Aktarma**: İstediğiniz tabloyu CSV formatında dışa aktarabilirsiniz.

## Kurulum

1. Projeyi klonlayın: `git clone https://github.com/kullanici/arac-kiralama.git`
2. Gerekli Kütüphaneleri indirin
3. Uygulamayı başlatın: `python main.py`

## Ekran Görüntüleri

![Ana Sayfa](/screenshots/anasayfa.png)
_Ana sayfa, müşteri girişi için bir form içerir._

![Araç Listesi](/screenshots/arac-listesi.png)
_Müsait araçların listelendiği bir ekran._

## Veritabanı Yapısı

Proje, SQLite veritabanı kullanır ve aşağıdaki tabloları içerir:

- `musteri`: Müşteri bilgilerini saklar.
- `arabalar`: Araç bilgilerini saklar.
- `kiralama`: Kiralama işlemlerine ait detayları saklar.
