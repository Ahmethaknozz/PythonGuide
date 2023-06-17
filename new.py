'''
website= "http://www.sadikturan.com"
course = "python kursu: bastan sona python programlama rehberiniz (40 saat)"

print(len(course))
print(website[7:10])
print(website[22:25])
#print(course [0:15], [-15:-1] )
result = course[-15:]
print(result)
result = course[::-1]
print(result)


name, surname, age, job = 'bora','yılmaz',32,'muhendis'

a = f'benim adim {name} {surname}, yasim{age} ve meslegim{job} '
print(a)

a = 'hello world'
b=a.replace('w','W')
print(b)


a = 'abc' * 3
print(a)
'''
'''
message = 'hello dear, my name is sadik turan'
message = message.upper()
message = message.lower()
message = message.title()
message = message.capitalize()
message = message.strip()
message = message.split()
message = message.split(',') #virgülden ayrıldı cümle ilk kısım 0. index virgülden sonraki kısım 2. index
message = '*'.join(message)
message.find('sadik')
message.startswith('h')
message.endswith('n')
message = message.replace('sadik','cinar')
message = message.center(100)

print(message)
print(message[0]) #0. index e ulaşmak için
'''

website = "https://www.sadikturan.com"
course= "Python kursu: bastan sona python programlama rehberiniz (40 saat)"
'''
a = ' hello world '
print(a.strip())

print(website[12:22])

print(course.lower())

b= website.count('a')
print(b)

print(website.startswith('www'), website.endswith('com'))

print(course.isalpha(),course.isdigit())
'''

#c= 'contents'
#print(c.center(50,'*'))

#print(course.replace(' ','-'))

a= 'hello world'
print(a.replace('world','there'))

print(course.replace(' ',''))
