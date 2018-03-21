#######1

satisMiktari=500
birimSatisFiyati=20
ciro=5000
i=1
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
i=1
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
    meCS=int(input("Haftalık Çalışma Saatini Giriniz:"))
    if (meCS==22):
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
i=1
while(dÜrün!=40):
    dÜrün=int(input("Defolu Ürün Sayısını Giriniz:"))
    if (dÜrün>=40):
        print("Defolu ürün sayısı günlük üretilen ürün sayısının yüzde 20 sinden fazladır.")  
    else:
        x=(i*dÜrün)
        print("Toplam defolu ürün:",x,"---",i,"günlük defolu ürün sayısı")
        i=i+1
        
