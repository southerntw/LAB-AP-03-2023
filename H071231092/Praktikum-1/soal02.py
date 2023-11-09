# Input Celsius
print("Konversi Suhu dari Celsius ke Kelvin, Reamur dan Fahrenheit")
celsius = int(input("Masukkan Suhu dalam Celcius : "))

# Rumus Celsius ke Kelvin, Reamur dan Fahrenheit
kelvin = int(celsius + 273)
reamur = int(celsius * 0.8)
fahrenheit = int(celsius * 1.8 + 32)

# Output hadil
print(f'Hasil konversi dari suhu {celsius} derajat Celsius ke Kelvin adalah : {kelvin}K')
print(f'Hasil konversi dari suhu {celsius} derajat Celsius ke Reamur adalah : {reamur}R')
print(f'Hasil konversi dari suhu {celsius} derajat Celsius ke Fahrenheit adalah : {fahrenheit}F')