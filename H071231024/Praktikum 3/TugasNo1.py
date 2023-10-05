print(
    "\nProgram Menghitung Jumlah Suku Fibonacci\n========================================"
)

inUser = int(input("Masukkan Jumlah Suku Yang Ingin Dihitung : "))
a = 0
b = 1

for i in range(inUser):
    print(a, end=" ")
    res = a + b
    a = b
    b = res
