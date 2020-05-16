"""
kümeleri tanımlamak için set() sınıfını kullanıyoruz
TANIM
kume=set()
şeklinde
-Kümeler içerisinde listeleri, demetleri,sayıları kullanabilriiz
kume=set(["asdas",1,2],2,3,"ali",("mehmet"))
ama
sayi= 10  kume=set(sayi) yapamam
yazi = "aasdawdasdasd "
kume = set(yazi)
print(kume)
{'w', 's', 'd', ' ', 'a'} --- çıktı
kume={"ali","veli","49"}
print(type(kume))#<class 'set'>
kume1={}
print(type(kume1))#bu şekilde boş küme oluşturamam bunu dict olarak algılar kume=set() bu şekilde olması lazım <class 'dict'>

for i in dir(kume):
    print(i)

add
clear
copy
difference
difference_update
discard
intersection
intersection_update
isdisjoint
issubset
issuperset
pop
remove
symmetric_difference
symmetric_difference_update
union
update

"""
kume = set([1,2,3,4,5])
kume.add(6)
print(kume)
kume.remove(2)#olmayan bir eleman yazsaidim  remove hata verirdi
print(kume)
kume.discard(2)#discard eleman var yada yok bakmaz direkt çıkartır
print(kume)

a = set([1,2,4,5])
b = set([2,4,5,6,7,8])

print(5*"======================")
print(a.difference(b))#a' nın b den farkı
print(b.difference(a))

print(b.intersection(a))# kesişim
