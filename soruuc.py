def ybsbir():
    global etkilesimBir
    begenib=365000
    yorumb=65000
    paylasimb=870
    icerikb=500
    takipcib=1125000
    etkilesimBir=(((begenib+yorumb+paylasimb)/icerikb)/takipcib)*100
    if etkilesimBir>0.20:
        print("Başarılı")
    else:
        print("Başarısız")
    return etkilesimBir
def ybsiki():
    global etkilesimIki
    begenii=450000
    yorumi=25000
    paylasimi=380
    iceriki=100
    takipcii=1450000
    etkilesimIki=(((begenii+yorumi+paylasimi)/iceriki)/takipcii)*100
    if etkilesimIki>0.20:
        print("Başarılı")
    else:
        print("Başarısız")
    return etkilesimIki
def ybsuc():
    global etkilesimUc
    begeniu=582000
    yorumu=52000
    paylasimu=1200
    iceriku=650
    takipciu=2000000
    etkilesimUc=(((begeniu+yorumu+paylasimu)/iceriku)/takipciu)*100
    if etkilesimUc>0.20:
        print("Başarılı")
    else:
        print("Başarısız")
    return etkilesimUc

