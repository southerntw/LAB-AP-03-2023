kata = str(input("Masukkan kata: "))
x = len(kata)

if x%2 != 0: 
    hasil = kata[0] + kata[x//2] + kata[-1]
else:
    hasil = kata[0] + kata[x//2 -1] + kata[x//2] + kata[-1]
print(hasil)