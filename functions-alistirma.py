'''
def yazdir(kelime,adet):
    print(kelime*adet)
yazdir('merhaba\n',10)

def parametre(*params):  #sinirisiz sayıda icerik girecegimiz icin * koyduk
    liste=[]
    for a in params:
        liste.append(a)
    return liste
b= parametre(10,20,'fgh')
print(b)


sayi1= int(input('Sayi1: '))
sayi2= int(input('Sayi2: '))

def asalsayilarbul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):  # +1 dendi cünkü eger son sayi da asal secilmisse onu da yazsin diye mesela 17 gibi
        if sayi > 1:
            for i in range(2,sayi):
                if sayi%i==0:
                    break
            else:
                print(sayi)

asalsayilarbul(sayi1,sayi2)


def tambölens(sayi):
    liste=[]
    for a in range(2,sayi):
        if (sayi%a==0):
            liste.append(a)
    return liste
        
a=tambölens(20)
print(a)
'''
b=int(input('bölen: '))
def kalanbul(a):
    c=a%b
    print(c)
kalanbul(10)



    
    





    