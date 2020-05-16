liste=["Onur","Askin","Python","Ogreniyor","Ogreniyor","Ogreniyor","Ogreniyor","Ogreniyor"]
liste.append("İns Cnm Yha")
liste.append("Yoh artık")
liste.remove("Yoh artık")

def listele(liste):

    for i in liste:
        print(i)

#liste2=liste# hafızada aynı yeri gösterir böyle bir eşitlik
#print(liste.count("Ogreniyor"))# kaç adet bulunduğunu söyler
liste2= []
print("Durum1")
print(liste)
print(liste2)
print(30*"=")
print("Durum2")
liste.remove("Python")
liste.remove("Ogreniyor")
liste.append("Ekle")
liste2.append("Ekle 2")
print(liste)
print(liste2)
print(30*"=")
print("Durum3")
print(30*"=")
liste2=liste.copy()
print(liste)
print(liste2)
liste.append("Ekle")
liste2.append("Ekle 2")
print(liste)
print(liste2)
