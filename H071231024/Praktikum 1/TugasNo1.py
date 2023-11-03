jdl = '\nProgram Menghitung Luas Permukaan dan Keliling Segitiga XYZ'
grs = '==========================================================='
print(f'{jdl}\n{grs}')

print('\nMenghitung Luas Permukaan dan Keliling Segitiga XYZ!')
X = float (input('Masukkan Panjang Sisi X : '))
Y = float (input('Masukkan Panjang Sisi Y : '))
Z = (X ** 2 + Y ** 2) ** 0.5

Keliling = X + Y + Z
Alas = X * Y * 0.5

print(f'Luas Permukaan : {Alas:.2f}')
print(f'Keliling : {Keliling:.2f}')