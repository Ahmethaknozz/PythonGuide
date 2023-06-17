'''
x=0
while x<100:
    if x%2==0:  # 100 e kadar cift sayilar
        print(f'sayi cift: {x}')
    else:
        print(f'sayi tek: {x}') #100 e kadar tek sayilar
    x+=1
print('done')


name= '' #false
while not name.strip: #strip bastan ve sondan bosluk karakterlerini siler
    name= input('isim:')
print(f'merhaba {name}')

sayilar= [1,3,5,7,9,12,19,21]
a=0
while a<len(sayilar):
    print(sayilar[a])
    a+=1


baslangic= int(input('baslangic: '))
bitis= int(input('bitis: '))
i=baslangic
while i<bitis:
    i+=1
    if i%2==1:
        print(i)

i=100
while i>0:
    print(i)
    i-=1

numbers=[]
i=0
while i<5:
    sayi= int(input('sayi: '))
    numbers.append(sayi)
    i+=1
numbers.sort
print(numbers)
'''
urunler=[]
adet=int(input('adet: '))
i=0
while i<adet:
    name= input('ürün ismi: ')
    price=int(input('ürün fiyat: '))
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f'ürün adi: {urun["name"]} ürün fiyati: {urun["price"]} ')






