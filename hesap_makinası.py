#Hesap Makinesi2
def toplama(sayilar):
    return sum(sayilar)
def cikarma(sayilar):
    result = sayilar[0]
    for num in sayilar[1:]:
        result -= num
    return result
def carpma(sayilar):
    result = 1
    for num in sayilar:
        result *= num
    return result
def bolme(sayilar):
    result = sayilar[0]
    for num in sayilar[1:]:
        if num == 0:
            print("Sıfıra bölme hatası!")
            return None
        result /= num
    return result

def hesap_makinesi():
    print("Hesap Makinesine Hoş Geldiniz!")
    print("İşlemler:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")
    print("Çıkış için 'q' tuşuna basınız.")

    while True:
        sayilar = []
        global secim
        secim = input("Lütfen bir işlem seçin (1/2/3/4) veya çıkmak için 'q' tuşuna basınız: ")
        if secim == 'q':
            print("Hesap makinesinden çıkılıyor...")
            break

        if secim not in ['1', '2', '3', '4', 'sayilar']:
            #inputla sayı veya sembol olarak ne alırsan al yinede string olarak dönüyo 
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
            continue

        while True:
            sayi = input("Lütfen bir sayı girin veya işlem yapmak için '=' tuşunu girin: ")
          
            if sayi == '=':
                if len(sayilar) < 2:
                    print("İşlem yapmak için en az iki sayı girmeniz gerekir!")
                    continue
                break
            try:
                sayilar.append(float(sayi))
            except ValueError:
                print("Geçersiz bir sayı girdiniz! Lütfen tekrar deneyin.")
                continue

        if secim == '1':
            print("Sonuç: ", toplama(sayilar))
        elif secim == '2':
            print("Sonuç: ", cikarma(sayilar))
        elif secim == '3':
            print("Sonuç: ", carpma(sayilar))
        elif secim == '4':
            sonuc = bolme(sayilar)
            if sonuc is not None:
                print("Sonuç: ", sonuc)
            else:
                continue
        elif secim == 'sayilar':
            print('girdiğiniz sayılar ise:' ,sayilar)
        
hesap_makinesi()
print('en son yaptığınız işem ise:', secim)