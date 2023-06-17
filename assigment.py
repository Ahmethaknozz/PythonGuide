
'''
x ,y ,z = 5,10,20

x+=5  # =  x = x +5 bu iki yontem ayni diger 4 işlem icin de ayni
x%=5  # kisa yol mod alma icin de gecerli  , y**=4 üssü 4 demektir  , illa sayısal deger olmasına gerek yok

values = 1,2,3,4,5
print(values)
x,y,*z= values  #* z ye atadı geri kalan elemanlari
print(x,y,z)
'''

x,y,z = 2,5,10

numbers= 1,5,7,10,6
#a=int(input('1.sayi giriniz: '))
#b=int(input('2.sayi giriniz: '))

#c=a*b-(x+y+z)
#print(c)

#print(y//x)

x,*y,z = numbers
print(x,y,z)
a=z**3
print(a)
a= y[0]+y[1]+y[2]
print(a)








