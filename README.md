
# Araç Kiralama Uygulaması (Rent Car OOP GUI)

Araba kiralama uygulaması, Python programlama dili kullanılarak geliştirilen ve grafik kullanıcı arayüzü (GUI) tasarımını bir araya getirerek, araç kiralama süreçlerini yönetebilen bir yazılımın nasıl oluşturulacağını gösterir. Kodun temelinde, nesne tabanlı programlama (OOP) prensipleri ve SQLite veritabanı kullanımı bulunmaktadır.

![image](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-1.png)

## Kullanılan Sınıflar ve OOP Prensipleri
## Araba Sınıfı:

### Encapsulation (Kapsülleme):
Araba sınıfı, özelliklerini (marka, model, yıl, kilometre) ve bu özelliklere erişim yöntemlerini içerir. Bu sayede, sınıfın iç yapısını gizleyerek dış dünyadan gelebilecek olası değişikliklere karşı koruma sağlanır.

![image](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-3.png)

### Inheritance (Kalıtım): 
Elektrikli Araba ve Benzinli Araba sınıfları, Araba sınıfından türetilmiştir. Bu sayede, temel özellikleri Araba sınıfından miras alarak, kod tekrarı önlenir ve kodun genişletilebilirliği artar.

### Abstraction (Soyutlama): 
Araba sınıfı, soyut bir sınıftır. İçerisinde soyut bir metot olan "bakim" metodu bulunur. Araç tipine özel bakım sürecini soyut olarak tanımlayarak yöntemin alt sınıflara göre uygulanması gerektiğini belirtir.

![image](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-5.png)

## Elektrikli Araba ve Benzinli Araba Sınıfları:

### Inheritance (Kalıtım): 
Her iki sınıf da Araba sınıfından türetilmiştir. Bu sayede, her iki sınıf da Araba sınıfının özelliklerini ve metotlarını kullanabilir.


### Polymorphism (Çok Biçimlilik): 
Her iki alt sınıf, Araba sınıfının soyut metodu olan "bakim"ı kendi ihtiyaçlarına göre uygular. Aynı isimli metodun farklı davranışlar sergilemesine olanak tanır.

## Kiralama Sınıfı
Kiralama sınıfı, bir kiralama işlemini temsil eder. Bu sınıf, kiralama işleminde kullanılan özellikleri ve bu işlemin ücretlendirilmesini içerir.

## Araç Kiralama Uygulaması Sınıfı
Bu sınıf, uygulamanın ana penceresini yönetir. Müşteri girişi, veritabanı bağlantısı, ana pencerenin oluşturulması ve araç listesinin gösterilmesi gibi temel işlevselliği içerir.


## Özellikler

- **Müşteri Girişi**: Kullanıcıların adlarını girerek sisteme giriş yapmalarını sağlar.
- **Araç Listesi**: Kullanıcıların kiralayabileceği arabaların listesini görüntüler.
- **Araç Kiralama**: Müşterilerin seçtikleri araçları belirli bir süre için kiralayabilmelerini sağlar.
- **Veritabanı Entegrasyonu**: SQLite veritabanı üzerinde müşteri, araç ve kiralama bilgilerini saklar.
- **Tablo Dışa Aktarma**: Veritabanındaki bilgileri CSV formatında dışa aktarma (export) imkanı sunar.

## GUI Ekran Görüntüleri

![Ana Sayfa](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-9.png)
![Ana Sayfa](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-10.png)
![Ana Sayfa](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-11.png)

## Veritabanı Yapısı

Proje, SQLite veritabanı kullanır ve aşağıdaki tabloları içerir:

- `musteri`: Müşteri bilgilerini saklar.
- `arabalar`: Araç bilgilerini saklar.
- `kiralama`: Kiralama işlemlerine ait detayları saklar.

## Veritabanı Ekran Görüntüleri
![Müşteri Tablosu](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-6.png)
![Arabalar Tablosu](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-7.png)
![Kiralama Tablosu](https://github.com/nazli-d/Rent-a-car-oop/blob/main/image/img-8.png)


# Katkıda Bulun
Projeye star vermek için aşağıdaki adımları takip edebilirsiniz:
1. Projenin GitHub sayfasına gidin.
2. Sayfanın sağ üst köşesinde bulunan "Star" düğmesine tıklayın.
3. Eğer oturum açmadıysanız, GitHub hesabınızla oturum açmanız istenecektir. Oturum açın veya yeni bir GitHub hesabı oluşturun.
4. "Star" düğmesine tekrar tıklayarak projeye katkıda bulunabilirsiniz.


