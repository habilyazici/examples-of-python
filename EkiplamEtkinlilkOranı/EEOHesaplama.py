from Ana import kullan,performans,kalite,eeo
# Alınan veriler ise kullanılan dosya kısmında olsun çünkü ana fonksiyonları bir kez kuracaksın Sonrasında tüm değişiklikler kullanılan dosya'dan olacak.
# Fonksiyonu print ettiğinde işlemler sadece printte kalıyor bu sorundan kurtulmak için fonksiyonu Başka bir değişkene atarsın ve o değişkeni kullanırsın

planUretimSure = float(input('Lütfen plan üretim süresini giriniz: '))
plansizDurus = float(input('Lütfen plansız duruş süresini giriniz: '))

standcevzam= float(input('Lütfen standart cevap zamanını giriniz: '))
uretimMik= float(input('Lütfen üretim miktarını giriniz: '))

saglamUrunMik= float(input('Lütfen sağlam ürün miktarını giriniz: '))
toplamUrunMİk= float(input('Lütfen toplam ürün miktarını giriniz: '))

k = kullan(planUretimSure, plansizDurus)
p = performans(standcevzam, uretimMik, planUretimSure)
q = kalite(saglamUrunMik, toplamUrunMİk)

print('Ekipman Etkinlik Oranı: ', eeo(k, p, q))