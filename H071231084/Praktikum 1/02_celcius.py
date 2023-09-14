#Konversi Suhu Dari Celcius ke Kelvin, Reamur, dan Fahrenheit
print("Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit")

C = int(input("Masukkan Suhu dalam Celcius: ")) 

K = C + 273
R = 4/5 * C
F = (9/5 * C) + 32

print(f"Hasil konversi dari suhu {C} derajat Celcius ke Kelvin adalah : {int(K)}K")
print(f"Hasil konversi dari suhu {C} derajat Celcius ke Reamur adalah : {int(R)}R")
print(f"Hasil konversi dari suhu {C} derajat Celcius ke Fahrenheit adalah : {int(F)}F")