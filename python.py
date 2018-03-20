####1.SORU
print("Katma Değer Ciro:")
def katmaDegerCiroHesapla(a,b,c,d,e):
    f=a-(b+c+d+e)
    if(f>1000):
        print(f,"/İşletme Katma Değer Cirosu Yüksek.")
    elif(500<f<999):
        print(f,"/İşletme Katma Değer Cirosu Normal.")
    else:
        print(f,"/İşletmenin Katma Değer Cirosu Düşük.")
a=int(input("Toplam Satış Miktarınız:"))
b=int(input("Hammadde Maliyeti:"))
c=int(input("Bakım Onarım Gideriniz:"))
d=int(input("Sevkiyat Gideriniz:"))
e=int(input("Satın Alınan Hizmet Giderleriniz:"))
katmaDegerCiroHesapla(a,b,c,d,e)

####2.SORU
print("Fark:")
def m2016(x,y):
    global z
    z=x/y
    return z
def m2017(a,b):
    global t
    t=a/b
    return t
def musteriFark(t,z):
    w=t-z
    print("2016-2017 Yılları Arası Müşteri Farkı:",w)
    return w
z=int(input("Müşterilerle Çalışma Süresini Hesaplayacanız Yıl:"))
x=int(input("2016/Çalışılan Süre:"))
y=int(input("2016/Toplam Müşteri Sayısı:"))
t=int(input("Müşterilerle Çalışma Süresini Karşılaştıracağınız Yıl:"))
a=int(input("2017/Çalışılan Süre:"))
b=int(input("2017/Toplam Müşteri Sayısı:"))

mCSa=m2016(x,y)
mCSy=m2017(a,b)
mFark=musteriFark(t,z)

####3.SORU
#x=Yazılım Geliri
#y=Finansman Geliri
#z=Ürün Satış Geliri

#a=Çalışan Maaşları
#b=Kira Gideri
#c=Donanım Maliyeti

#f=Yazılım Geliri
#g=Sponsorluk Geliri
#h=E-Ticaret Geliri
#j=Ürün Satış Geliri

#k=Çalışan Maaşları
#l=Kira Gideri
#m=Bakım Maliyeti

print("İlk 6 aylık ve son 6 aylık gelir-gider kalemleri:")
def ilkAltıGelir(x,y,z):
    global t
    t=x+y+z
    print("İlk Altı Aylık Gelir:",t)
    return t
def ilkAltıGider(a,b,c):
    global d
    d=a+b+c
    print("ilk Altı Aylık Gider:",d)
    return d
def ilkAltıKar(t,d):
    global ilkKar
    ilkKar=t-d
    print("İlk Altı Aylık Kar:",ilkKar)
    return ilkKar
def sonAltıGelir(f,g,h,j):
    global v
    v=f+g+h+j
    print("Son Altı Aylık Gelir:",v)
    return v
def sonAltıGider(k,l,m):
    global n
    n=k+l+m
    print("Son Altı Aylık Gider:",n)
    return n
def sonAltıKar(v,n):
    global sonKar
    sonKar=v-n
    print("Son Altı Aylık Kar:",sonKar)
    return sonKar
def islKar(ilkKar,sonKar):
    global isletmeKar
    isletmeKar=ilkKar-sonKar
    if (isletmeKar>5000):
        print("İşletme Çok Karlıdır.")
    elif (5000>isletmeKar>1000):
        print("İşletme Karı Normaldir.")
    else:
        print(isletmeKar,"=İşletme Yeterince Karda Değildir.")
    return isletmeKar


x=int(input("Yazılım Gelirini Giriniz:"))
y=int(input("Finansman Gelirini Giriniz:"))
z=int(input("Ürün Satış Gelirini Giriniz:"))
a=int(input("Çalışan Maaşlarını Giriniz:"))
b=int(input("Kira Giderini Giriniz:"))
c=int(input("Donanım Maliyetini Giriniz:"))
f=int(input("Yazılım Gelirini Giriniz:"))
g=int(input("Sponsorluk Gelirini Giriniz:"))
h=int(input("E-Ticaret Gelirini Giriniz:"))
j=int(input("Ürün Satış Gelirini Giriniz:"))
k=int(input("Çalışan Maaşlarını Giriniz:"))
l=int(input("Kira Giderini Giriniz:"))
m=int(input("Bakım Maliyetini Giriniz"))

ilkGelir=ilkAltıGelir(x,y,z)
ilkGider=ilkAltıGider(a,b,c)
kar=ilkAltıKar(t,d)
sonGelir=sonAltıGelir(f,g,h,j)
sonGider=sonAltıGider(k,l,m)
kars=sonAltıKar(v,n)
iKari=islKar(ilkKar,sonKar)

####4.SORU
def donemBasiStok(a=100,b=100,c=100):
    global d
    d=a+b+c
    print("Dönembaşı Stok Durumu:",d)
    return d
def donemIciStok(k,y,z):
    global t
    t=k+y+z
    print("Dönem İçi Stok Durumu:",t)
    return t
def donemSonuStok(e,f,g):
    global h
    h=d+t-(e+f+g)
    print("Dönemsonu Stok Durumu:",h)
    return h
def ortalamaStok(d,t,h):
    o=(d+h)/2
    print("Ortalama Stok Değeri:",o)
    return o

k=int(input("Dönemiçi Alınan Koltuk Sayısı:"))
y=int(input("Dönemiçi Alınan Yatak Sayısı:"))
z=int(input("Dönemiçi Alınan Dolap Sayısı:"))
e=int(input("Dönemsonu Satılan Koltuk Sayısı:"))
f=int(input("Dönemsonu Satılan Yatak Sayısı:"))
g=int(input("Dönemsonu Satılan Dolap Sayısı:"))

donemB=donemBasiStok(a=100,b=100,c=100)
donemI=donemIciStok(k,y,z)
donemS=donemSonuStok(e,f,g)
ortalamaS=ortalamaStok(d,t,h)

