# Input sisi x dan y
print("Menghitung luas permukaan dan keliling segitiga")
x = float(input("Panjang sisi x : "))
y = float(input("Panjang sisi y : "))
z = (x**2 + y**2)**0.5

# Rumus luas dan keliling segitiga
luas_segitiga = y*x/2
keliling_segitiga =  x + y + z

# Output
print(f'Luas permukaan : {luas_segitiga:.2f}')
print(f'Keliling : {keliling_segitiga:.2f}')

