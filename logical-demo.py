'''
x= 6
result = 5< x<10
print(result)

result= x>5 and x<10


result = (x>0) or (x<5)

x=6
result= ((x>5) and (x<10)) and (x%2==0)


a= int(input('bir sayi giriniz : '))
result= (a>0) and (a<100)
print=(f'sayi 0-100 arasındamı? :{result}')



a= int(input('bir sayi giriniz : '))

b= (a>0) and (a%2==0)
print(f'sayi pozitif cift bir sayimidir: {b}')


email= 'ahmet1'
password= '123'
a=input('emailinizi giriniz: ')
b=input('pass giriniz: ')
c= (email==a) and (password==b)
print('giriş yapma durumunuz:', c)


a=int(input('sayi1: '))
b=int(input('sayi2: '))
c=int(input('sayi3: '))
result= (a>b) and (a>c)
print(f'a en buyuk sayidir: {result} ')

result= (b>a) and (b>c)
print(f'b en buyuk sayidir: {result} ')

result= (c>a) and (c>b)
print(f'c en buyuk sayidir: {result} ')



vize1=float(input('1.vize: '))
vize2=float(input('2.vize: '))
final=float(input('final: '))
ort= ((vize1+vize2)/2)*0.6 + (final*0.4)
#a= (ort>=50) and (final>=50)

a=(ort>=50) or (final>=70)
print(f'kalma durumunuz: {a}')


print(f'not ort: {ort} ve gecme durumu: {a}')
'''


name=input('isim: ')
weight=float(input('kilo: '))
height=float(input('boy: '))

index= weight/ (height**2)

zayıf= (index>=0) and (index<=18.4)
normal=(index>=18.5) and (index<=24.9)
fazlakilolu=(index>=25.0) and (index<=29.9)
sisman=(index>30.0) and (index<34.9)


print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen zayıf: {zayıf}')
print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen normal: {normal}')
print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen fazlakilolu: {fazlakilolu}')
print(f'{name} kilo indeksin: {index} ve kilo degerlendirmen sisman: {sisman}')








