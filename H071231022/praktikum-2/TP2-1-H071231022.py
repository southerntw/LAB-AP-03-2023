print('Pilih Gender Anda')
print('1.Pria')
print('2.Wanita')

gender = int(input('='))
             
berat = float(input('Masukan Berat Badan (kg) ='))
tinggi_awal =float(input('Masukan Tinggi Badan (cm) ='))

tinggi = tinggi_awal/100 #dri cm ke m
BMI = (berat/(tinggi**2))

if gender == 1:
    if BMI <18:
        print(f'Anda Tergolong Underweight dengan BMI {BMI:.2f}')
    elif 18<= BMI <=22.3:
        print(f'Anda Tergolong Normal dangan BMI {BMI:.2f}')
    elif 24<= BMI <=26.9:
        print(f'Anda Tergolong Overweight dengan BMI {BMI:.2f}') 
    else:
        print(f'Anda Tergolong Obese dengan BMI {BMI:.2f}')
elif gender == 2:
    if BMI <17:
        print(f'Anda Tergolong Underweight dengan BMI {BMI:.2f}')
    elif  17<= BMI <=23.9:
        print(f'Anda Tergolong Normal dangan BMI {BMI:.2f}')
    elif  24<= BMI <=27.9:
        print(f'Anda Tergolong Overweight dengan BMI {BMI:.2f}') 
    else:
        print(f'Anda Tergolong Obese dengan BMI {BMI:.2f}')