import soruiki
a=int(input("Kasa Hesabi:"))
b=int(input("Alinan cekler:"))
c=int(input("Bankalar:"))
d=int(input("Alacak Senetleri:"))
e=int(input("Ticari Senetler:"))
donen_varlik=soruiki.donenVarlik(a,b,c,d,e)
print(donen_varlik)
x=int(input("Binalar:"))
y=int(input("Tasitlar:"))
z=int(input("Demirbaslar:"))
duran_varlik=soruiki.duranVarlik(x,y,z)
print(duran_varlik)
k=int(input("Banka Kredileri:"))
l=int(input("Saticilar:"))
kisa_vadeli=soruiki.kisaVadeli(k,l)
print(kisa_vadeli)
p=int(input("Banka Kredileri:"))
o=int(input("Borc Senetleri:"))
uzun_vadeli=soruiki.uzunVadeli(p,o)
print(uzun_vadeli)
n=int(input("Sermaye:"))
oz_kaynak=soruiki.ozKaynak(n)
print(oz_kaynak)
toplamPa=soruiki.toplam_pa(kisa_vadeli,uzun_vadeli,oz_kaynak)
print(toplamPa)
toplamAk=soruiki.toplam_ak(donen_varlik,duran_varlik)
print(toplamAk)

if toplamPa==toplamAk:
    print("Kapanis bilancosu dogru hesaplanmistir.")
else:
    print("Bilanco yanlis hesaplanmistir")


