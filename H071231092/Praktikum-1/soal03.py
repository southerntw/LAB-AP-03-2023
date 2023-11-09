# Input nilai a, b dan c
a = float(input("Input a : "))
b = float(input("Input b : "))
c = float(input("Input c : "))

# Rumus
x1 = (-b+(b**2 - 4*a*c)**0.5)/(2*a)
x2 = (-b-(b**2 - 4*a*c)**0.5)/(2*a)


# Output hasil
print(f'x1 = {x1:.2f}')
print(f'x2 = {x2:.2f}')