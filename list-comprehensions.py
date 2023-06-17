'''
numbers=[x for x in range(10)]
print(numbers)

numbers= [x**2 for x in range(10) if x%3==0]
print(numbers)


mystr= 'hello'
mylist= []
for a in mystr:
    mylist.append(a)
print(mylist)

mylist= [a for a in mystr]
print(mylist)


result= [x if x%2==0 else 'tek' for x in range(1,10)]
print(result)


numbers=[ (x,y)for x in range(3) for y in range(3)]
print(numbers)

a=[]
for x in range(3):
    for y in range(3):
        a.append((x,y))
print(a)
'''