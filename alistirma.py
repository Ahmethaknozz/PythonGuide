import random

sayi= (random.randint(10,30))
can= int(input('kac hak olsun? : '))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin= int(input('sayi: '))
    if sayi==tahmin:
        print(f'bildiniz. {sayac}. hakta. toplam puan:{100-(100/can)*(sayac-1)}')
        break
    elif sayi<tahmin:
        print('yazdiğiniz sayi büyüktür')
    else:
        print('yazdiğiniz sayi kücüktür')
    if hak==0:
        print(f'hakkiniz bitti. tutulan sayi:{sayi}')



