
import os
kitapListe=[]
kitap=("İnce Mehmet","Yaşar Kemal")
menu="""
[1] Kitap Ekle
[2] Kitap Al
[3] Tümünü Listele
[Q] Çıkış

"""
def kitapEkle(kitapİsmi:tuple,my_list:list):
    my_list.append(kitapİsmi)
    print("Ekleme islemi Tamamlandı")
    print("ANA MENÜ İÇİN ENTER . . . ")
    input()

def kontrol(kitap:tuple,my_list:list):
    if kitap in list:
        return True
    else:
        return False

def kitapCikar(kitap:tuple,my_list:list):
    if kontrol(kitap,my_list):
        my_list.remove(kitap)#kitap cıkartılıyor
        print("Kitap Çıkartma işlemi Tamamlandı . . .")
        print("ANA MENÜ İÇİN ENTER . . . ")
        input()
    else:
        print("Arattığınız kitap mevcut değildir ")
        print("ANA MENÜ İÇİN ENTER . . . ")
        input()


def listele(liste:list):
    for i in liste:
        print("Kitap Adı : {} -----------> Yazar : {}".format(i[0],i[1]))

while True:
    os.system("cls")#----> terminal ekranını temizliyor
    print(menu)
    secim=input("İsleminizi seciniz : ")

    if secim == "1":
        kitapAdi=input("Ekleyeceğiniz kitap ismi : ")
        kitap_yazari=input("Ekleyeceğiniz kitabın yazarı : ")
        kitap = (kitapAdi,kitap_yazari)
        kitapEkle(kitap,kitapListe)#kitap ekleniyor
    elif secim=="2":
        kitapAdi = input("Silceğin kitap ismi : ")
        kitap_yazari = input("Siliceğiniz  kitabın yazarı : ")
        kitap = (kitapAdi, kitap_yazari)
        kitapCikar(kitap, kitapListe)
    elif secim=="3":
        listele(kitapListe)
    elif  secim=="q" or secim=="Q":
         print("Keyifli okumalar . . . . . .")
         quit()
    else:
        print("Hatalı Giriş yaptınız . . . ")
