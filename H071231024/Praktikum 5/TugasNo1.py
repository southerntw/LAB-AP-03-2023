s1 = input("\nMasukkan Karakter 1 : ")
s2 = input("Masukkan Karakter 2 : ")
s2 = "".join(reversed(s2))

tm = ""

for i in range(len(s1)):
    tm += s1[i] + s2[i]
print(f"Hasil Mixed = {tm}")
