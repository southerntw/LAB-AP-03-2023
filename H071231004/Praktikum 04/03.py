def maximum(x):
    maximum = x[0]
    for i in x:
        if maximum < i:
            maximum =  i
    return maximum

x = [0, 3, 1, 2, 5, 4, 7, 1, 6, 8, 5]
print('>>', maximum(x))

# nilai = input('Masukkan Nilai (pisahkan dengan spasi): ')
# nilai_list = [int(x) for x in nilai.split()]
# print('Nilai maximum:', maximum(nilai_list))