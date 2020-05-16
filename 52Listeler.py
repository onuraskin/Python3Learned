from builtins import print


##kitapListe=list()
string="a"
string +="b"
##print(string)
#liste veri tipleri içinde hertürlü veri tipini tutabilir int string float  liste

Listem=["abc",3,3.51,[3,5,12]]
#for i in Listem:
   # print(i)
    #print(type(i))



kitapListe = ["İnce Mehmet","ÇanakkaleGeçilmez","Python","Java"]
for i in kitapListe:
    print("Kitabın adı : {}".format(i))

eklenecek=input("Kitabın ismi : ")
kitapListe+=eklenecek
print(kitapListe) #öğeleri ayrı ayrı bastırır
eklenecek=input("Kitabın ismi : ")
kitapListe+=[eklenecek] # bu şekilde yazdırmalıyım ki cümleyi harf harf değilde direkt alsın
print(kitapListe)



