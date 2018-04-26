from module import isletmeKari
from module import adambasiCiro

gelir=int(input("Gelirleri giriniz:"))
gider=int(input("Giderleri giriniz:"))
toplamCiro=int(input("Toplam ciroyu giriniz:"))
toplamCalisanSayisi=int(input("Adambaşı ciroyu giriniz:"))

isletme_kari=isletmeKari(gelir,gider)
adambasi_ciro=adambasiCiro(toplamCiro,toplamCalisanSayisi)
print(isletme_kari)
print(adambasi_ciro)
