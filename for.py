'''
numbers= [1,2,3,4,5]
for a in numbers:
    print('hello')

name='hakan'
for a in name:
    print(a)


tuple= [(1,2),(1,3),(3,5)]

for a,b in tuple:
    print(a,b,a)


d= {'k1':1,'k2':2,'k3':3}
for a in d.items():
    print(a)


sayilar = [1,3,5,7,9,12,19,21]
for a in sayilar:
    if a%2!=0:
        print(a)

sayilar = [1,3,5,7,9,12,19,21]
b=0
for a in sayilar:
    b+=a
print(b)


sayilar = [1,3,5,7,9,12,19,21]
for tek in sayilar:
    if tek%2!=0:
        a=tek**2
        print(a)


sehirler= ['kocaeli','istanbul','ankara','izmir','rize']
for a in sehirler:
    if len(a)<=5:
        print(a)

urunler= [
    {'name':'s1','price':3000},
    {'name':'s2','price':4000},
    {'name':'s3','price':5000},
    {'name':'s4','price':6000},
    {'name':'s5','price':7000},
]
c=0
for a in urunler:
    b=a['price']
    c+=b
print(c)
'''

urunler= [
    {'name':'s1','price':3000},
    {'name':'s2','price':4000},
    {'name':'s3','price':5000},
    {'name':'s4','price':6000},
    {'name':'s5','price':7000},
]
for a in urunler:
    b= a['price']
    if b<=5000:
        print(a['name'])

    
    




