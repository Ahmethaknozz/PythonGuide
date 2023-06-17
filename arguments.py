'''
def change(n):
    n[0]= 'istanbul'
sehirler= ['ankara','izmir']  # change bizim atadigimiz it metod yerine istersek ahmet de diyebilirdik
#change(sehirler)
#print(sehirler)

def change(n):
    n[0]='istanbul' #kopya bir liste oluşturduk
sehirler=['ankara','izmir']
n=sehirler[0:2] #0. index ten 2. ye kadar. bunun yerine [:]desek de yeterlidir . yani böylelikle orjinal listeye ulaşiriz
n[0]='istanbul'
print(sehirler)
print(n)


def add(a,b):
    return sum((a,b)) #sum pythonun kendi kütüphanesine olan bir metoddur toplama yapar
print(add(10,20))

def add(*params): # tek * kullandık cünkü tuple tipinde
    return sum(params)
print(add(10,20,5,30,40,35,80))
'''
def displayuser(**params):  # ** kullandık dictionary olacagi icin
    for key, value in params.items():
        print('{} is {}'.format(key,value))



displayuser(name='cinar',age=20, city='erzincan')
displayuser(name='ada',age=12, city='izmit',phone=123)