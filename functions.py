'''
def sayHello(name):
    return 'hello'+name
a=sayHello('hakan')
    
print(a)


def total(num1,num2):
    return num1+num2
a= total(10,20)
print(a)


def yashesapla(dyili):
    return 2021-dyili
agecinar= yashesapla(2017)
agehakan= yashesapla(2000)
agemehmet= yashesapla(1999)
print(agecinar,agehakan)

def emeklilikkacil(dyili,isim):    
    
    DOCSTRING:doğum yiliniza göre emekliliginize kac yil kaldi
    İNPUT: Dogum Yili
    OUTPUT:Hesapalanan yil bilgisi


    
    yas = yashesapla(dyili)
    emeklilik= 65-yas

    if emeklilik>0:
        print(f'emeklilike {emeklilik} yil kaldi')
    else:
        print('zaten emeklisiniz')


print(help(emeklilikkacil))
emeklilikkacil(1983,'hakan')


def toplam(a,b):
    print('toplaminiz', a+b)
toplam(1,5)


def toplam(a,b):
    return a+b
c = toplam(2000,2500)
print(c)
'''
a=[1,2,3,4,5]
for b in a:
    print('selam')
