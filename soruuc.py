def etkilesimOrani(begeni,yorum,paylasim,icerik,takipci):
    global etkilesim
    etkilesim=(((begeni+yorum+paylasim)/icerik)/takipci)*100
    if etkilesim>0.20:
        print("Başarılı")
    else:
        print("Başarısız")
    return etkilesim

