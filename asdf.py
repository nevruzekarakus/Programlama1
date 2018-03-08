def oeeHesapla():
    x=int(input("Planlanmış Üretim Süresini Giriniz:"))
    y=int(input("Plansız Duruş Süresini Giriniz:"))
    z=int(input("Standart Çevrim Süresini Giriniz:"))
    t=int(input("Üretim Miktarını Giriniz:"))
    u=int(input("Sağlam Ürün Miktarını Giriniz:"))
    v=int(input("Toplam Üretim Miktarını Griniz:"))
    o=1
    ku=(x-y)/x
    if x!=y:
        per=(z*t)/(x-y)
        ka=u/v
        oee=ku*per*ka*o
        print("%",oee)
    else:
        print("Üretim Süresi ile Duruş Süresi aynı olamaz.")
    
    
