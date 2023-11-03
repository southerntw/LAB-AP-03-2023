#Program Mixed Kata
kata1 = input('Masukkan Kata Pertama: ').lower()
kata2 = input('Masukkan Kata Kedua: ').lower()
kata2 = "".join(reversed(kata2))
hasil = ""
x = min(len(kata1), len(kata2))
for i in range(x):
    hasil = hasil + kata1[i] + kata2[i]
hasil += kata1[x:] + kata2[x:]
print(f'Hasil Mixed Kata: {hasil}')