import sqlite3

baglanti = sqlite3.connect("rent-a.db")
cursor = baglanti.cursor()

# Müşteri tablosu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS musteri (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ad_soyad TEXT
    )
''')

# Araba tablosu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS arabalar (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        marka TEXT,
        model TEXT,
        yil INTEGER,
        tip TEXT,
        durumu TEXT DEFAULT 'müsait',
        kilometre INTEGER DEFAULT 0  
    )
''')

# Kiralama tablosu
cursor.execute('''
    CREATE TABLE IF NOT EXISTS kiralama (
        musteri_id INTEGER,
        araba_id INTEGER,
        kiralama_tipi TEXT,
        sure INTEGER,
        ucret INTEGER,
        durumu TEXT DEFAULT 'kiralandı',
        FOREIGN KEY (araba_id) REFERENCES arabalar (id),
        FOREIGN KEY (musteri_id) REFERENCES musteri(id)
    )
''')

# Elektrikli Arabalar
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Tesla', 'Model S', 2023, 'Elektrikli', 500)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Porsche', 'Taycan', 2023, 'Elektrikli', 20000)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Audi', 'e-tron', 2023, 'Elektrikli', 3000)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Mercedes-Benz', 'EQC', 2023, 'Elektrikli', 0)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Jaguar', 'I-PACE', 2023, 'Elektrikli', 15000)")

# Benzinli Arabalar
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Mercedes-Benz', 'S-Class', 2023, 'Benzinli', 1500)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('BMW', '7 Series', 2023, 'Benzinli', 32100)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Lexus', 'LS', 2023, 'Benzinli', 48000)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Audi', 'A8', 2023, 'Benzinli', 0)")
cursor.execute("INSERT INTO arabalar (marka, model, yil, tip, kilometre) VALUES ('Porsche', 'Panamera', 2023, 'Benzinli', 0)")

baglanti.commit()
# Veritabanı bağlantısını kapat
baglanti.close()
