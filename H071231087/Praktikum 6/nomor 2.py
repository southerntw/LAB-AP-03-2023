a1 = list(map(int, (input("Masukkan array ke-1 : ").split())))
a2 = list(map(int, (input("Masukkan array ke-2 : ").split())))
a1 = set(a1)
a2 = set(a2)
x = a1.intersection(a2)
xtuple = tuple(x)
p = len(xtuple)
if p > 0:
    print(f"Terdapat {p} buah duplikat yaitu {xtuple}")
else:
    print(f"Tidak ada duplikasi ditemukan.")  