# Mengubah String dengan mengambil kata pertama, tengah dan akhir
kata = input("Masukkan Kata : ")
y = len(kata)
if y % 2 != 0:
    x = kata[0] + kata[y//2] + kata[-1]
else:
    x = kata[0] + kata[y//2-1] + kata[y//2] + kata[-1]
print(x)