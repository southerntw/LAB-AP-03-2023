# menghitung BMI berdasarkan gender

jenis_kelamin = int(input("Pilih Gender Anda \n1. Pria\n2. Wanita\n= "))
tinggi = int(input("Masukkan tinggi badan (cm) = "))
berat = float(input("Masukkan berat badan (kg)= "))
tinggikemeter = tinggi/100
bmi = berat/((tinggikemeter)**2)
print(f"{bmi:.2f}")
if jenis_kelamin == 1:
    if bmi < 18:
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif bmi >= 18 and bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi >= 24 and bmi < 27:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    elif bmi >= 27:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}");
elif jenis_kelamin == 2:
    if bmi < 17:
        print(f"Anda tergolong Underweight dengan BMI {bmi:.2f}")
    elif bmi >= 17 and bmi < 24:
        print(f"Anda tergolong Normal dengan BMI {bmi:.2f}")
    elif bmi >= 24 and bmi < 28:
        print(f"Anda tergolong Overweight dengan BMI {bmi:.2f}")
    elif bmi >= 28:
        print(f"Anda tergolong Obese dengan BMI {bmi:.2f}");
else:
    print("tidak valid")