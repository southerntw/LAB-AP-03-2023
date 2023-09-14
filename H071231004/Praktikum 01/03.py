import math 
print('Menyelesaikan Persoalan Persamaan Kuadrat')

#masukkan nilai a,b,c 
a = float(input('Input Nilai a ='))
b = float(input('Input Nilai b ='))
c = float(input('Input Nilai c ='))

# masukkan rumus diskriminan
D = (b*b) - (4*a*c)
if(D>0):
    x1 = (-b + math.sqrt (D)) / (2*a)
    x2 = (-b - math.sqrt (D)) / (2*a)

    print('x1 =', round(x1,2))
    print('x2 =', round(x2,2))

elif(D==0):
    x1 = (-b + math.sqrt (D)) / (2*a)
    x2=x1

    print('x1 =', round(x1,2))
    print('x2 =', round(x2,2))

else:
    print('(akar tidak real/imajiner)')