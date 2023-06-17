
def Topla(x, y):
   return x + y
 

def Cikar(x, y):
   return x - y
 

def Carp(x, y):
   return x * y
 

def Bol(x, y):
   return x / y

def Islem():
    
    print("işlem seciniz (1) Toplama (2) Çıkartma (3) Çarpma (4) Bölme")

    
    secim = input("işlem seciiniz")

    
    sayi1 = int(input("1. Sayıyı girin : "))
    sayi2 = int(input("2. Sayıyı girin : "))

   
    if secim == '1':
        print(sayi1,"+",sayi2,"=", Topla(sayi1,sayi2)) 
    elif secim == '2':
        print(sayi1,"-",sayi2,"=", Cikar(sayi1,sayi2)) 
    elif secim == '3':
        print(sayi1,"*",sayi2,"=", Carp(sayi1,sayi2)) 
    elif secim == '4':
        print(sayi1,"/",sayi2,"=", Bol(sayi1,sayi2))
    else:
        print("Geçersiz bir işlem numarası girdiniz.")


while True:
    Islem()

