#konversi suhu dari celcius ke kelvin,reamur,farhreinheit
celcius = int(input('masukan suhu ='))

kelvin = int (celcius + 273) #rumus
reamur = int((4/5)*celcius)
fahrenheit = int((9/5)*celcius+32)

print(f'hasil konversi {celcius} celcius ke kelvin = {kelvin}k')
print(f'hasil konversi {celcius} celcius ke reamur = {reamur}r')
print(f'hasil konversi {celcius} celcius ke fahrenheist = {fahrenheit}f')
