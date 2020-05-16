print("""
    [1] - Toplama 
    [2] - Çıkarma
    [3] - Bölme 
    [4] - Çarpma 
    [0] - Çıkış 
	""")
     


     giris = input(" Seçiminiz : ")
     giris=int(giris)
	
    if giris == 1 :
		x=input("İlk Sayi : ")
		x=float(x)
		y=input("İkinci Sayi : ")
		y=float(y)

		print(" İşlem Sonucu ", x+y)
    if giris == 2 :
		x=input("İlk Sayi : ")
		x=float(x)
		y=input("İkinci Sayi : ")
		y=float(y)
		
		print(" İşlem Sonucu ", x-y)
    if giris == 3 :
		x=input("İlk Sayi : ")
		x=float(x)
		y=input("İkinci Sayi : ")
		y=float(y)
		
		print(" İşlem Sonucu ", x/y)
    if giris == 4 :
		x=input("İlk Sayi : ")
		x=float(x)
		y=input("İkinci Sayi : ")
		y=float(y)
		
		print(" İşlem Sonucu ", x+y)
      if giris == 0 :
		 exit():


