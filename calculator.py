print("Hesap makinesine hoş geldin!")

while True:

    sayi1 = float(input("Birinci sayıyı gir: "))
    sayi2 = float(input("İkinci sayıyı gir: "))

    print("Yapmak istediğin işlemi seç:")
    print("1 - Toplama")
    print("2 - Çıkarma")
    print("3 - Çarpma")
    print("4 - Bölme")

    secim = input("Seçimin (1/2/3/4): ")

    if secim == "1":
        print("Sonuç:", sayi1 + sayi2)

    elif secim == "2":
        print("Sonuç:", sayi1 - sayi2)

    elif secim == "3":
        print("Sonuç:", sayi1 * sayi2)

    elif secim == "4":
        if sayi2 != 0:
            print("Sonuç:", sayi1 / sayi2)
        else:
            print("Bir sayı 0'a bölünemez!")

    else:
        print("Geçersiz seçim yaptın.")

    tekrar = input("Yeni işlem yapmak ister misin? (e/h): ")

    if tekrar.lower() == "h":
        print("Program kapatılıyor...")
        break
