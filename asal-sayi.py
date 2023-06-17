'''
sayi= int(input('sayi giriniz: '))
if sayi==1:
    print('1 asal degildir')
for a in range(2,sayi):
    if sayi%a==0:
        print('sayi asal degildir')
        break
else:
    print('sayi asaldir')
'''

asalsayılar=[]
for a in range(1,100):
    for asal1 in range(2,a):
        if a%asal1==0:
            break
        elif a%asal1!=0 and asal1 ==a-1:
            asalsayılar.append(a)
            
            

for i in asalsayılar:
    print(i,end=".")