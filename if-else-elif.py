'''
isim=input('isim: ')
yas=int(input('yasiniz: '))
egitim=input('egitim dur: ')
if yas>=18:
    if egitim== 'lise' or egitim== 'uni':
        print('kosullariniz uygundur')
    else:
            print('kosullariniz egitim yetersizidr')


else:
    print('kosullariniz yas yetersizidr')


yazili1=float(input('1.yazili: '))
yazili2=float(input('2.yazili: '))
sozlu=float(input('sözlü: '))
ort= (yazili1+yazili2+sozlu)/3
if  0<=ort<25:
    print('noyunuz:0')
elif 25<=ort<45:
    print('notunuz:1')
elif 45<=ort<54:
    print('notunuz:2')
elif 55<=ort<=100:
    print(f'not ort:{ort} , ders notu:5')
else:
    print('yanlis giris yaptiniz')
'''
import datetime


tarih= input('kac gundur trafiktesiniz (2019/8/9): ')
tarih= tarih.split('/')


trafigecikis= datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi= datetime.datetime.now()
fark= simdi- trafigecikis
print(simdi)

