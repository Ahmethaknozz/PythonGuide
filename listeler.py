

'''
markalar= ['bmw','mercedes','opel','mazda']
markalar[3] = 'toyota'
print(markalar)
a = 'mercedes' in markalar
print(a)
print(markalar[-2])
a= markalar[0:3]
print(a)
markalar[-2:] = ['toyota','renault']
print(markalar)
b= markalar + ['audi','renault']
print(b)
#del markalar[-1]
print(markalar)
c= markalar[::-1]

studenta= ['yigit','bilgi',2010 , [70,60,70]]
studentb= ['sena','turan',1999, [80,80,70]]
studentc= ['ahmet','turan',1998,[80,70,90]]

ab= f"{studenta[0]} bilgi {2021-studenta[2]} yasinda ve not ort {(studenta[3][0] + studenta[3][1] + studenta[3][2]) // 3}"
print(ab)



numbers = [1,10,5,16,4,9,10]
letters= ['a','g','s','b','y','a','s']

print(min(numbers))
print(max(numbers))
print(max(letters))
print(min(letters))
'''
names = ['ali','yagmur','hakan','deniz']
years = [1998,2000,1998,1987]

#names.append('cenk')
#names.insert(0,'sena')
#names.remove('deniz')
#names.pop(4) 
#a = names.index('deniz')
#a= 'ali' in names
#names.reverse()
#names.sort()
#years.sort()
str = 'chevrolet','dacia'
a=years.count(1998)
years.clear()


#print(years)

markalar = []

marka=input('marka: ')
markalar.append(marka)

marka=input('marka: ')
markalar.append(marka)

marka=input('marka: ')
markalar.append(marka)



print(markalar)







#print(max(years), min(years))
#print(list(str))

