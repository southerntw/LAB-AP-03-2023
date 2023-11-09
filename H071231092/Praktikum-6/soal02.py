# # Cara pake map
# input_array1 = input("Input array ke-1: ")
# array1 = set(map(int, input_array1.split()))

# input_array2 = input("Input array ke-2: ")
# array2 = set(map(int, input_array2.split()))

# hasil = (array1 & array2)

# print(f"Terdapat {len(hasil)} buah duplikat yaitu {tuple(hasil)}")


# # Tidak pake map
# array1 = {1, 2, 3, 4, 5}
# array2 = {6, 2, 3, 7, 8}

# hasil = (array1 & array2)

# print("Input array ke-1:"," ".join(str(item) for item in array1))
# print("Input array ke-2:"," ".join(str(item) for item in array2))

# print(f"Terdapat {len(hasil)} buah duplikat yaitu {tuple(hasil)}")


input_array1 = input("Input array ke-1: ")
array1 = set()
for item in input_array1.split():
    array1.add(int(item))

input_array2 = input("Input array ke-2: ")
array2 = set()
for item in input_array2.split():
    array2.add(int(item))

hasil = (array1 & array2)

if len(hasil) == 1:
    print(f"Terdapat {len(hasil)} buah duplikat yaitu ({hasil.pop()})")
elif len(hasil) > 1:
    print(f"Terdapat {len(hasil)} buah duplikat yaitu {tuple(hasil)}")
else :
    print("Tidak ada duplikat !!")

