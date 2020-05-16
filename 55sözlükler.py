"""sozluk={"home":"ev",
        "book": 100,
         "pen":"kalem"}
print(sozluk)
print(sozluk["home"])
print("Pen'in Türkçe Anlamı : {}".format(sozluk["pen"]))"""

karekter={"ad":"Warrior",
          "can": 500,
          "güc":100,
          "silah": "Two Handed Sword"}

print("Karekterin Adı    : {}".format(karekter["ad"]))
print("Karekterin Canı   : {}".format(karekter["can"]))
print("Karekterin Silahi : {}".format(karekter["silah"]))
print("Karekterin Gücü   : {}".format(karekter["güc"]))

karekter2={"ad":"Staff",
          "can": 250,
          "güc":400,
          "silah": "Two Handed Staff"}

print("Karekterin Adı    : {}".format(karekter2["ad"]))
print("Karekterin Canı   : {}".format(karekter2["can"]))
print("Karekterin Silahi : {}".format(karekter2["silah"]))
print("Karekterin Gücü   : {}".format(karekter2["güc"]))

def vuran(vuran:dict,vurulan:dict):
    eksilen=vuran["güc"]
    vurulan["can"] = vurulan["can"]-eksilen

vuran(karekter,karekter2)
vuran(karekter2,karekter)


print("1 Karekterin Adı    : {}".format(karekter["ad"]))
print("1 Karekterin Canı   : {}".format(karekter["can"]))
print("1 Karekterin Silahi : {}".format(karekter["silah"]))

print("2 Karekterin Adı    : {}".format(karekter2["ad"]))
print("2 Karekterin Canı   : {}".format(karekter2["can"]))
print("2 Karekterin Silahi : {}".format(karekter2["silah"]))






