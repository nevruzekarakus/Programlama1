#######1

satisMiktari=500
birimSatisFiyati=20
ciro=5000
i=0
while True:
    satisMiktari=satisMiktari+200
    birimSatisFiyati=birimSatisFiyati+10
    ciro=satisMiktari*birimSatisFiyati
    i=i+1
    if (ciro>500000):
        print(i/12,"Yıl Sonra Ciro 500.000TL'den Fazla Olur.")
        break

#######2

sstok=10000
satisM=500
alisM=100
i=0
while True:
    sstok=sstok+alisM-satisM
    i=i+1
    if (sstok==0):
        print(i,". Ayda Stok Sıfırlanacaktır.")
        break
    
########3

girilen=""
k=0
while(girilen!=0):
    girilen=int(input("Bir Sayı Giriniz. Bitirmek için '0':"))
    if (girilen==0):
        print("Program sonlandırıldı.")
    else:
        girilen=float(girilen)
        print("Bölümden kalanların toplamı:",girilen%3)
        k=k+(girilen%3)
        print("Toplam:",k)

#######4

calisan=50
meCS=""
ahaYev=90*4*7
ameYev=(90*0.10)
i=22
while(meCS!=22):
    meCS=int(input("1.Hafta Mesai Çalışma Saatini Giriniz:"))
    meCS1=int(input("2.Hafta Mesai Çalışma Saatini Giriniz:"))
    meCS2=int(input("3.Hafta Mesai Çalışma Saatini Giriniz:"))
    meCS3=int(input("4.Hafta Mesai Çalışma Saatini Giriniz:"))
    
    if (meCS+meCS1+meCS2+meCS3>=22):
        print("Aylık Mesai Saatini Geçtiğinden Hesaplanamaz.")
    else:
        meCS=int(meCS)
        x=calisan*((ahaYev)+(meCS*ameYev*4))
        print("Aylık Ödenen Toplam Maaş:",x)
        
    i=i+1
#haftanın yedi günü çalışıyor varsayalım.


#######5
gPantolon=200
dÜrün=""
i=0
while True:
    dÜrün=int(input("Defolu Ürün Sayısını Giriniz:"))
    i=i+1
    if (dÜrün<40):
        print(i,"günlük defolu ürün sayısı")
    else:
        print("Defolu ürün sayısı günlük üretilen ürün sayısının yüzde 20 sinden fazladır.")
        break
        
