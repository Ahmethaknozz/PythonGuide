'''
import datetime
tarih= input('kac gundur trafiktesiniz (2019/8/9): ')
tarih= tarih.split('/')
trafigecikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi= datetime.datetime.now()
fark= simdi - trafigecikis
days= fark.days
if days<=365:
    print('okey')
else:
    print('yanlis')


a= int(input('sayi: '))
if 0<a<100:
    print(f'{a}  0 ile 100 arasindadir')
else:
    print(f'{a} 0 ile 100 arasinda degildir')


a= int(input('sayi: '))
if a>0:
    if a%2==0:
        print('a pozitif cift sayidir')
    else:
        print('a pozitif tek sayidir')
elif a<0:
    if a%2==0:
        print('a negatif cift sayidir')
    else:
        print('a negatif tek sayidir')
else:
    print('girdiginiz sayi tanımsizdir')



email= 'abc'
passw= '123'
a=input('email girin: ')
b=input('passw girin: ')
if a==email:
    if b==passw:
        print(' giris basarili')
    else:
        ('yanlis passw girisi')
else:
    print('yanlis email girisi')

a=int(input('1.sayi'))
b=int(input('2.sayi'))
c=int(input('3.sayi'))
if a>b and a>c:
    print('a en büyük sayidir')
elif b>a and b>c:
    print('b en büyük sayidir')
else:
    print('c en buyuk sayidir')


vize1= float(input('1.vize: '))
vize2= float(input('2. vize: '))
final=float(input('final: '))
ort= (vize1+vize2)*0.6 + final*0.4
if ort>=50:
    if final>=50:
        print('ort ve final den gectiniz')
    else:
        print('final notunuz yetersizdir')
else:
    print('basarisiz')
'''

name=input('adiniz: ')
kg=float(input('kilonız: '))
hg=float(input('boyunuz: '))
index= (kg)/(hg**2)
if 0<index<18.4:
    print(f'{name} :zayif')
elif 18.5<=index<=24.9:
    print(f'{name} :normal')
elif 25<=index<=29.9:
    print(f'{name} :kilolu')
elif 30<=index<=35:
    print('obez')
else:
    print('bilgiler yanlis')








    
