x=0
result=0
while x<=100:
    x+=1
    if (x%2)==0:
        continue #devam ettirir
    result+=x
    
print(f'toplam: {result}')

