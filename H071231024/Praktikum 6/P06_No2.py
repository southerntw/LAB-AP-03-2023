arr1 = input("Input Array Ke-1: ").split()
arr2 = input("Input Array Ke-2: ").split()

arr1 = [int(num) for num in arr1]
arr2 = [int(num) for num in arr2]


duplikat = set()

for num in arr1:
    if num in arr2:
        duplikat.add(num)


if len(duplikat) > 0:
    print("Terdapat", len(duplikat), "Buah Duplikat Yaitu", tuple(duplikat))
else:
    print("Tidak Ada Duplikasi Ditemukan.")
