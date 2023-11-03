#Menentukan Luas dan Keliling Segitiga
print("Menghitung Luas dan Keliling Segitiga")

t = float(input("Masukkan tinggi segitiga: "))
a = float(input("Masukkan alas segitiga: "))
m = (a**2 + t**2) ** 0.5

luas = (a*t) / 2
keliling = a+t+m

print(f'Luas Permukaan: {luas: .2f}')
print(f'Keliling: {keliling: .2f}')