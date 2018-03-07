#1.Soru
def kar():
    x=int(input("Finansman Gelirini Giriniz:"))
    y=int(input("Pazar Gelirini Giriniz:"))
    z=int(input("Kira Gelirini Giriniz:"))
    u=x+y+z
    a=int(input("Ücreti Giriniz:"))
    b=int(input("Finansman Giderini Giriniz:"))
    c=int(input("Pazar Giderini Giriniz:"))
    d=int(input("Kira Giderini Giriniz:"))
    e=int(input("Muhasebe Giderini Giriniz:"))
    v=a+b+c+d+e
    t=u-v
    if (t<1000):
        print("Kar sağlanmamıştır.")
    else:
        print("Kar sağlanmıştır.")
    return t

#yada

##
##x=int(input("Finansman Gelirini Giriniz:"))
##y=int(input("Pazar Gelirini Giriniz:"))
##z=int(input("Kira Gelirini Giriniz:"))
##u=x+y+z
##a=int(input("Ücreti Giriniz:"))
##b=int(input("Finansman Giderini Giriniz:"))
##c=int(input("Pazar Giderini Giriniz:"))
##d=int(input("Kira Giderini Giriniz:"))
##e=int(input("Muhasebe Giderini Giriniz:"))
##v=a+b+c+d+e
##t=u-v
##if (t<1000):
##    print("Kar sağlanmamıştır.")
##else:
##    print("Kar sağlanmıştır.")


#2.Soru
def oeeHesapla():
    x=int(input("Planlanmış Üretim Süresini Giriniz:"))
    y=int(input("Plansız Duruş Süresini Giriniz:"))
    z=int(input("Standart Çevrim Süresini Giriniz:"))
    t=int(input("Üretim Miktarını Giriniz:"))
    u=int(input("Sağlam Ürün Miktarını Giriniz:"))
    v=int(input("Toplam Üretim Miktarını Griniz:"))
    ku=(x-y)/x
    if x!=y:
        per=(z*t)/(x-y)
    else:
        print("Üretim Süresi ile Duruş Süresi aynı olamaz.")
    ka=u/v
    o=1.0
    oee=ku*per*ka*o
    print("%",oee)

#3.Soru

def adambasiCiro():
    x=int(input("Satış Miktarını Giriniz:"))
    y=int(input("Birim Satış Fiyatını Giriniz:"))
    tcs=25
    ciro=x*y
    adambCiro=ciro/tcs
    return adambCiro


#yada

##x=int(input("Satış Miktarını Giriniz:"))
##y=int(input("Birim Satış Fiyatını Giriniz:"))
##tcs=25
##ciro=x*y
##adambCiro=ciro/tcs
##print("Adambaşı Ciro=",adambCiro)

