from module import isletmeKari
from module import adambasiCiro

gelir=int(input("Gelirleri giriniz:"))
gider=int(input("Giderleri giriniz:"))
isletme_kari=isletmeKari(gelir,gider)
print(isletme_kari)
toplamCiro=int(input("Toplam ciroyu giriniz:"))
toplamCalisanSayisi=int(input("Adambaşı ciroyu giriniz:"))
adambasi_ciro=adambasiCiro(toplamCiro,toplamCalisanSayisi)
print(adambasi_ciro)
