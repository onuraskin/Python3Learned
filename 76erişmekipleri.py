"""
'r' ----------> okuma
'w' ---------->yazma
'a'  ----------> yazma
'x'  ----------> yazma (Varsa Hata Verir) tamamen boş olmasını istiyor varsa da hata veriyor


'r+' ----------> Okuma ve Yazma(dosyanın Var olması gerekir )
'w+' ----------> Okuma ve Yazma(Varsa siler )
'a+' ---------->Okuma ve Yazma
'x+' ---------->Okuma ve Yazma

"""
dosya=open("deneme1.txt","a")#dosya varsa kaldığı yerden devam eder
dosya.write("\n deneme satiri 4 ")
dosya=open("deneme1.txt","a+")
dosya.write("\n deneme satiri  ")
dosya.close()