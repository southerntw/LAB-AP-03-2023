# Mentukan luas dan keliling

x = float(input('Masukkan nilai x: '))
y = float(input('Masukkan nilai y: '))
z = (x**2+y**2)**0.5


luas = (x*y)/2 
keliling =  x + y + z

print(f'Luas segitiga adalah {luas:.2f}')
print(f'Keliling segitiga adalah {keliling:.2f}')