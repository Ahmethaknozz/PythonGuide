'''
a,b,c,d= 5,5,10,4

result=(a==a)
result= (a==c)

print(result)

a= int(input('1 sayi giriniz: '))
b= int(input('1 sayi giriniz: '))

c= (a>b)
print(f'a:{a} b:{b} den büyüktür : {c} ')

a= float(input('1. vizeyi giriniz: '))
b= float(input('2. vizeyi giriniz: '))
c= float(input('finali giriniz: '))
ort= ((a+b) /2) *0.6 + c*0.4
sonuc= ort>=50
print(f'ort notunuz: {ort} ve dersten gecme durumunuz: {sonuc}')



a=float(input('bir sayi giriniz: '))

result= a%2 == 0
print(f'sayinizin cift olma durumu: {result} ')


a=int(input('bir sayi giriniz: '))
b= a>0
c= a<0


email= 'ahmethakan.123'
passaword='abc123'
a=(input('parolanizi giriniz: '))
b= input('email giriniz: ')
c= email==b.lower().strip() #harfleri kücük yapıp oyle degerlendirir yani büyük harf yazsan bile onu dogru sayar, birde strip ekledik buda eger sonuna boşluk koyarsa o boşlıgu silip degerlendirir
d= passaword==a
print(f'emailinizin dogrulugu: {c} , pass in dogrulugu: {d}')

'''
a=1
a+=1
print(a)

