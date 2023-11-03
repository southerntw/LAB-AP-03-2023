print('Menghitung Luas Segitiga dan Keliling Segitiga')

#masukkan nilai x dan y 
x = float(input('Masukkan Nilai X:'))
y = float(input('Masukkan Nilai Y:'))

#rumus untuk mencari sisi miring (z)
z = (x**2 + y**2)**0.5

#rumus luas dan keliling segitiga 
luas = y*x*1/2
keliling = x + y + z 

print(f'Luas Segitiga = {luas:.2f}') #string formating 
print(f'Keliling Segitiga= {keliling:.2f}') 