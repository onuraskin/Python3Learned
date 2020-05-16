kitapListesi=[]
menu="""
1 - Kitap Ekle 
2 - Kitap Çıkar 
3 - Kitapları Listele
0 - Çıkış 

"""
def kitapEkle(kitap,liste):
    liste +=[kitap]
    print("Kitap Eklendi")
    input("Ana Menü için Entere bas")

def kitapCikar():
    pass
def kitaplarıListele(liste):
    for i in liste:
        print("Kitap adı ---->>>>>   {}".format(i))
        print("")

    input("Ana Menü için Entere bas")

def cik():
    quit()


while True:
    print(menu)
    secim=input("Seçiminiz ?")

    if secim=="1":
        kitapAdi=input("Kitap Adi")
        kitapEkle(kitapAdi,kitapListesi)

    elif secim=="2":
        kitapCikar()

    elif secim=="3":
        kitaplarıListele(kitapListesi)
    elif secim=="0":
        cik()
    else:
        print(": : : : : Hatalı girdi : : : : : ")
        input("Ana Menü için Entere bas")
