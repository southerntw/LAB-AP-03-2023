n = int(input("Masukkan jumlah suku Fibonacci: "))

x = 0
y = 1

for i in range (n):
    print(x, end=" ")
    z = x + y
    x = y
    y = z