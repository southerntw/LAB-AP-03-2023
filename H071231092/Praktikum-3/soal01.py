# Input berupa berapa banyak suku yang ingin dijumlahkan
suku = int(input(''))
a = 0
b = 1

if suku <= 1:
    print(a)
else:
    print(a,b,end=' ')
    for x in range(2,suku):
        c = a+b
        print(c, end=" ")
        a = b
        b = c