# Mencari Nilai X

a = float(input('a = '))

# Input
while a == 0: 
    print('Input Tidak Valid! ( a |= 0 )')
    a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

# Nilai X1
X1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f'X1 = {X1:.2f}')

# Nilai X2
X2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
print(f'X2 = {X2:.2f}')

