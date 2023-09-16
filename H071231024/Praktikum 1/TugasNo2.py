jdl = '\nProgram Mengkonversi Suhu'   #Celcius ke Kelvin, Reamur, dan Fahrenheit
grs = '========================='
print(f'{jdl}\n{grs}\n')

a = float(input('Konversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit!\nMasukkan Suhu dalam Celcius : '))
K = round(a + 273.15)                # K =  Kelvin
R = round(a * 4 / 5)                 # R = Reamur
F = round((a * 9 / 5) + 32)          # F = Fahrenheit

print(f'Hasil Konversi dari Suhu {round(a)} Derajat Celcius ke Kelvin adalah : {K}K')
print(f'Hasil Konversi dari Suhu {round(a)} Derajat Celcius ke Reamur adalah : {R}R')
print(f'Hasil Konversi dari Suhu {round(a)} Derajat Celcius ke Fahrenheit adalah : {F}F')


