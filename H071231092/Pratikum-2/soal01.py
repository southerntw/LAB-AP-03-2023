gender = input("Pilih Gender Anda\n1. Pria\n2. Wanita\nPilih(1-2) : ")
tinggi = float(input("Masukkan tinggi badan (cm) : "))
berat = float(input("Masukkan berat badan (kg) : "))

tinggi = tinggi/100

bmi = berat/(tinggi**2)

if gender == 1:
    if bmi < 18:
        print(f'Anda tergolong Underweight dengan BMI {bmi:.2f}')
    elif bmi  >= 18 and bmi <= 23.9:
        print(f'Anda tergolong Normal dengan BMi {bmi:.2f}')
    elif bmi  >= 24 and bmi <= 26.9:
        print(f'Anda tergolong Overweight dengan BMI {bmi:.2f}')
    else:
        print(f'Anda tergolong Obese dengan BMI {bmi:.2f}')
else:
    if bmi < 17:
        print(f'Anda tergolong Underweight dengan BMI {bmi:.2f}')
    elif bmi  >= 17 and bmi <= 23.9:
        print(f'Anda tergolong Normal dengan BMi {bmi:.2f}')
    elif bmi  >= 24 and bmi <= 27.9:
        print(f'Anda tergolong Overweight dengan BMI {bmi:.2f}')
    else:
        print(f'Anda tergolong Obese dengan BMI {bmi}') 