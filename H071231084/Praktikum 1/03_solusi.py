#Menghitung Solusi Persamaan Kuadrat
a = float(input("Input a = "))
if a == 0:
    print("Nilai a tidak boleh 0")
    exit()
b = float(input("Input b = "))
c = float(input("Input c = "))

X1 = (-b + ((b**2 - 4*a*c) ** 0.5)) / (2*a)
X2 = (-b - ((b**2 - 4*a*c) ** 0.5)) / (2*a)

print(f'X1= {X1: .2f}')
print(f'X2= {X2: .2f}')
