s1 = input("Masukkan String Pertama : ")
s2 = input("Masukkan String Kedua : ")
s2 = ''.join(reversed(s2))
m = "" #string kosong, tempat menaruhnya
panjang = min(len(s1), len(s2))

for i in range(panjang):
          m += s1[i] + s2[i]
m += s1[panjang:] + s2[panjang:]
print(m) 