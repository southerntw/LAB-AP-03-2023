#persamaan kuadrat
a = float(input('nilai a ='))
b = float(input('nilai b ='))
c = float(input('nilai c ='))

#rumus persamaan kuadrat
x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)

print(f' x1 = {x1:.2f}')
print(f' x2 = {x2:.2f}')
