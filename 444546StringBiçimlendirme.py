"""baslangic="buradan başlar "
son="burada biter"
string="burası orta kısım"

newString=baslangic + string + son
print(newString)

Bu çok ilkel bir yazım tarzıdır """
from builtins import print
""" 
cumle = """
"""English : Hello World
Türkçe  : {}  {} """
""".format("Merhaba","Dünya")

print(cumle)
karakterler="abcçdefg"

for i in karakterler:
    print("bastırılan karekterler : {}".format(i))
"""
degisken1="onur"
degisken2="askin"
ifade1="{ad} {soyad}".format(ad= degisken1,soyad =degisken2)
ifade2="{0} {1}".format(degisken1,degisken2)
print(ifade1)
print(ifade2)
"""
:> sağa yaslama
:< sola yaslama
:^ merkezde alan ayırma
:s yalnızca string ifade
:d yalnızca sayısal ifade
:b ikili sistemde karşılık
"""
degisken1="onur"
degisken2="askin"
ifade1="|{:>15}|".format(degisken1)
ifade2="|{:<15}|".format(degisken2)
ifade3="|{:^15}|".format(degisken2)
print(ifade1)
print(ifade2)
print(ifade3)

