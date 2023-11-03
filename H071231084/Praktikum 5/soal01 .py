str1 = str(input("Inputan Pertama: "))
str2 = str(input("Inputan Kedua: "))
str2 = "".join(reversed(str2))
str3 = ""
panjang = min(len(str1), len(str2))

for i in range (panjang):
    str3 += str1[i] + str2[i]
    
str3 += str1[panjang:] + str2[panjang:]
print(str3)