def donenVarlik():
    global donen
    a=20000
    b=10000
    c=5000
    d=28000
    e=65000
    donen=a+b+c+d+e
    return donen
def duranVarlik():
    global duran
    x=150000
    y=25000
    z=8000
    duran=x+y+z
    return duran
def kisaVadeli():
    global kisa
    k=42000
    l=60000
    kisa=k+l
    return kisa
def uzunVadeli():
    global uzun
    p=35000
    o=115000
    uzun=p+o
    return uzun
def ozKaynak():
    global oz
    n=59000
    m=0
    oz=m+n
    return oz
def toplam_pa():
    pasif=kisa+uzun+oz
    aktif=donen+duran
    if aktif==pasif:
        print("Kapanis bilancosu dogru hesaplanmistir.")
    else:
        print("Bilanco yanlis hesaplanmistir")
