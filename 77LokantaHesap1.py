import os
masalar = dict()
for i in range(10):
    masalar[i]=0 #9 masa oluşturdum 0 atadım

def hesapEkle():
    masaNo=int(input("Masa numaraniz kaç"))
    gecerliÜcret=masalar[masaNo]
    eklecenek=float(input("Eklenecek ücret nedir :  "))
    toplam=gecerliÜcret+eklecenek
    masalar[masaNo]=toplam

    return masalar[masaNo]
def hesapSil():
    masaNo = int(input("Masa numaraniz kaç"))
    gecerliÜcret = masalar[masaNo]
    eksilecek= float(input("Eksilecek ücret nedir :  "))
    toplam = gecerliÜcret - eksilecek
    masalar[masaNo] = toplam
    print("Masanın şuanki ücreti : ",masalar[masaNo])

def hesapKontrol(dosya_adi):

    try:
        dosya=open(dosya_adi)
        veriler=dosya.read()
        veriler=veriler.split("\n")
        veriler.pop()#son öğeyi sildim
        dosya.close()
        flag=True
    except FileNotFoundError:
        dosya = open(dosya_adi,"w")#ilk kez çalıştırdğımda oluşturucak
        dosya.close()
        flag=False

    if flag:
        for i in enumerate(veriler):#enumarate i değişkenine demet olarak verileri göndermemi sağladi
            masalar[i[0]]=float(i[1])
    else:
        pass



def kayitGuncelle():
    dosya=open("kayitlar.txt","w")
    for i in range(10):
        ucret=masalar[i]
        ucret=str(ucret)
        dosya.write(ucret+"\n")

    dosya.close()




def main():
    hesapKontrol("kayitlar.txt")
    while True:
        os.system("cls")
        print("""
        [1] Masaları Görüntüle
        [2] Hesap Ekle 
        [3] Hesap Sil
        [Q] Çıkış
    
        """)
        secim=input("İşleminiz nedir ? ")
        if secim=="1":
            for i in range(10):
                print("Masa {} için  hesap : {}".format(i,masalar[i]))
            print("İşlem Tamamlandı Ana menü İçin ENTER : ")
            input()
        elif secim=="2":
            x=hesapEkle()
            print("Mevcut Masa Ücreti : {}".format(x))
            print("İşlem Tamamlandı Ana menü İçin ENTER : ")
            input()
        elif secim== "3":
            hesapSil()
            print("İşlem Tamamlandı Ana menü İçin ENTER : ")
            input()
        elif secim=="q" or secim=="Q":
            print("Çıkıliyor ")
            quit()
        kayitGuncelle()




main()
