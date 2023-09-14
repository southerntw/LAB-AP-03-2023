print('Mengkonversi Suhu dari Celcius ke Kelvin, Reamur, dan Fahrenheit')

#memasukkan suhu dalam derajat celcius 
c = int(input('Masukkan Suhu dalam Celsius:'))

#rumus kelvin, reamur, dan fahrenheit 
kelvin =int(c + 273.15)
reamur = int(4 * c // 5)
fahrenheit = int(9 * c // 5 + 32) 

print('Hasil konversi dari {c} derajat Celcius ke Kelvin adalah', kelvin, 'K')
print('Hasil konversi dari {c} derajat Celcius ke Reamur adalah', reamur, 'R')
print('Hasil konversi dari {c} derajat Celcius ke Fahrenheit adalah', fahrenheit, 'F')