def kullan(planUretimSure, plansizDurus):
    return (planUretimSure - plansizDurus)/planUretimSure

def performans(standcevzam, uretimMik, planUretimSure):
    return (standcevzam*uretimMik)/planUretimSure
    
def kalite(saglamUrunMik, toplamUrunMİk):
    return saglamUrunMik/toplamUrunMİk

def eeo(kullan, performans, kalite):
    return (kullan*performans*kalite) / 100

def anafonksiyon():
    print('Şirket Kar hesaplama mekanizmamıza hoşgeldiniz')
    print("Makinemizde yapabileceğiniz işlemler şunlardır: 'Kullan', 'Performans', 'Kalite', 'Eeo'")
    liste= ['kullan', 'performans', 'kalite', 'eeo', 'q']
    while True:
        print('yapabileceğiniz işlemler', liste)
        mesaj = str(input('lütfen hesaplama yapmak istediğiniz türü seçiniz: veya çıkış için q ya basınız ')).lower()
        
        if mesaj in liste:

            if mesaj == 'kullan':
                planUretimSure = float(input('Lütfen plan üretim süresini giriniz: '))
                plansizDurus = float(input('Lütfen plansız duruş süresini giriniz: '))
                print('kullan :', kullan(planUretimSure, plansizDurus))

            elif mesaj == 'q':
                print('Çıkış işleminiz gerçekleşti.')
                break

            elif mesaj == 'performans':
                planUretimSure = float(input('Lütfen plan üretim süresini giriniz: '))
                standcevzam= float(input('Lütfen standart cevap zamanını giriniz: '))
                uretimMik= float(input('Lütfen üretim miktarını giriniz: '))
                print('performans :', performans(planUretimSure, standcevzam, uretimMik))

            elif mesaj == 'kalite':
                saglamUrunMik= float(input('Lütfen sağlam ürün miktarını giriniz: '))
                toplamUrunMİk=float(input('Lütfen toplam ürün miktarını giriniz: '))
                print('Kalite :', kalite(saglamUrunMik, toplamUrunMİk))

            elif mesaj == 'eeo':
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
        else:
            print('bir parametre seçmediniz lütfen bir parametre seçin')

anafonksiyon()