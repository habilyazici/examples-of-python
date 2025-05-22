# Dosya Yükleme ve Yönetimi Uygulaması

Bu proje, kullanıcıların PDF, PNG veya JPG dosyalarını yükleyip yönetebileceği basit bir web uygulamasıdır. Kullanıcılar kayıt olabilir, giriş yapabilir, dosya yükleyebilir, silebilir ve kendi dosyalarını listeleyebilirler. Her kullanıcıya özel dosya klasörü oluşturulur ve dosyalar güvenli şekilde saklanır.

## Özellikler

- Kullanıcı kayıt ve giriş (JWT tabanlı kimlik doğrulama, cookie ile)
- PDF, PNG, JPG/JPEG dosya yükleme
- Dosya listeleme ve silme
- Kullanıcıya özel dosya klasörü
- Maksimum dosya boyutu: 10 MB
- Hesap silme (tüm dosyalarla birlikte)
- Basit ve anlaşılır arayüz

## Kullanılan Teknolojiler

- Python 3.x
- Flask
- Flask-JWT-Extended
- Werkzeug (şifreleme ve güvenli dosya adı)
- HTML (Jinja2 ile şablonlama)

## Kurulum

1. **Depoyu klonlayın veya dosyaları indirin:**
    ```
    git clone <repo-url>
    cd <proje-dizini>
    ```

2. **Gerekli Python paketlerini yükleyin:**
    ```
    pip install flask flask-jwt-extended werkzeug
    ```

3. **Uygulamayı başlatın:**
    ```
    python app.py
    ```

4. **Tarayıcıda açın:**
    ```
    http://127.0.0.1:5000
    ```

## Kullanım

- **Kayıt Ol:** Ad, soyad, telefon, e-posta ve şifre ile kayıt olun.
- **Giriş Yap:** E-posta ve şifre ile giriş yapın.
- **Dosya Yükle:** PDF, PNG veya JPG dosyalarınızı yükleyin.
- **Dosya Sil:** Listeden dosya silin.
- **Çıkış Yap:** Güvenli şekilde çıkış yapın.
- **Hesap Sil:** Tüm dosyalarınızla birlikte hesabınızı silebilirsiniz.

## Güvenlik ve Notlar

- Dosya yükleme sırasında sadece izin verilen uzantılar kabul edilir.
- Her kullanıcıya özel klasör oluşturulur, başkalarının dosyalarına erişilemez.
- JWT tokenlar cookie ile saklanır ve kısa süreli geçerliliğe sahiptir.
- Maksimum dosya boyutu 10 MB ile sınırlandırılmıştır.

## Geliştirici Notları

- Kodun tamamı `app.py` dosyasındadır.
- Kullanıcı verileri `users.json` dosyasında saklanır.
- Arayüz dosyaları `templates` klasöründe yer almalıdır.

## Lisans

Bu proje eğitim ve değerlendirme amaçlıdır.
