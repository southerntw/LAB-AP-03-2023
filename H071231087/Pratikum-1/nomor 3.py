# menentukan persamaan kuadrat

a = int(input('masukkan nilai a = ' ))
b = int(input('masukkan nilai b = ' ))
c = int(input('masukkan nilai c = '))


a1 = b ** 2
b1 = (4*(a*c))
c1 = 2 * a

x1 = (-b + ((a1 - b1) ** 0.5))/c1
x2 = (-b - ((a1 - b1) ** 0.5))/c1


print(f'x1 = {x1:.03f}')
print(f'x2 = {x2:.03f}')
