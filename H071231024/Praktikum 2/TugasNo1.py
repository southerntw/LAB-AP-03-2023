print('Program Menghitung Body Mass Index (BMI)\n')

# MENENTUKAN GENDER, TINGGI BADAN, DAN BERAT BADAN
gender = int(input('Pilih Gender Anda:\n1. Pria\n2. Wanita\n= '))
tb = float(input('Masukkan Tinggi Badan (cm) : '))
bb = float(input('Masukkan Berat Badan (kg) : '))

# MENGKONVERSI TINGGI BADAN DARI CENTIMETER KE METER 
tbmeter = tb / 100

# RUMUS BMI
bmi = bb / tbmeter ** 2

# MENENTUKAN KATEGORI BMI
if gender == 1:
    if bmi < 18:
            print(f'Anda Tergolong Underweight dengan BMI {bmi:.2f}')
    elif 18 <= bmi <= 23.9:
            print(f'Anda Tergolong Normal dengan BMI {bmi:.2f}')
    elif 24 <= bmi <= 26.9: 
             print(f'Anda Tergolong Overweight dengan BMI {bmi:.2f}')
    elif bmi >= 27:
            print(f'Anda Tergolong Obese dengan BMI {bmi:.2f}')
if gender == 2:
    if bmi < 17:
            print(f'Anda Tergolong Underweight dengan BMI {bmi:.2f}')
    elif 17 <= bmi <= 23.9:
            print(f'Anda Tergolong Normal dengan BMI {bmi:.2f}')
    elif 24 <= bmi <= 27.9: 
            print(f'Anda Tergolong Overweight dengan BMI {bmi:.2f}')
    elif bmi >= 28:
            print(f'Anda Tergolong Obese dengan BMI {bmi:.2f}')

