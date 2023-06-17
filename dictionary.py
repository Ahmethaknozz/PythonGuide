#sehirler= ['kocaeli','istambul']
#plakalar= [41,34]
#print(plakalar[sehirler.index('kocaeli')])
#print(sehirler[plakalar.index(34)])

a= {
    'hakan':{
        'age':20,
        'surn':'oz'
    }
}

print(a['hakan']['surn'])

'''
users = {
    'hakan':{
        'age':20,
        'name':'khan'
    },
    'ahmet':{
        'age':21,
        'name':'ahm'
    }
}

print(users['ahmet']['age'])


ogrenciler = {
    '120': {
        'ad':'ali',
        'soyad':'yılmaz',
        'telefon': '532 000 00 01'
    } ,
    '125': {
        'ad':'can',
        'soyad':'korkmaz',
        'telefon':'532 000 00 02'
    },
    '128': {
        'ad':'volkan',
        'soyad':'yukselen',
        'telefon':'532 000 00 03'
    }
}


ogrenciler = {}
number= input("ogrenci num : ")
name = input("ogrenci adi : ")
surname= input("ogrenci soyadi : ")
phone= input("ogrenci telefon : ")

ogrenciler[number]  = {
    'ad':name,
    'soyad':surname,
    'telefon':phone
}


ogrenciler = {}
number= input("ogrenci num : ")
name = input("ogrenci adi : ")
surname= input("ogrenci soyadi : ")
phone= input("ogrenci telefon : ")

ogrenciler[number]  = {
    'ad':name,
    'soyad':surname,
    'telefon':phone
}



ogrenciler = {}
number= input("ogrenci num : ")
name = input("ogrenci adi : ")
surname= input("ogrenci soyadi : ")
phone= input("ogrenci telefon : ")

ogrenciler[number]  = {
    'ad':name,
    'soyad':surname,
    'telefon':phone
}


#print(ogrenciler)

print('*'*50)

ogrno= input("numaranizi giriniz : ")
ogr= ogrenciler[ogrno]

print(f'aradiginiz {ogrno} nolu ogrencinin adi : {ogr["ad"]} soyadi : {ogr["soyad"]} ve telefon nosu : {ogr["telefon"]}')

'''

















