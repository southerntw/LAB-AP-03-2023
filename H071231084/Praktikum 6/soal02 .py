list1 = list(map(int, (input("Masukkan array ke-1: ").split())))
list2 = list(map(int, (input("Masukkan array ke-2: ").split())))

list1 = set(list1)
list2 = set(list2)

dup = tuple(list1 & list2)
p = len(dup)

if p > 0:
    if p == 1:
        print(f"Terdapat 1 buah duplikat yaitu ({''.join(map(str, dup))})")
    else:
        print(f"Terdapat {p} buah duplikat yaitu {dup}")
else:
    print(f"Tidak ada duplikasi ditemukan")
