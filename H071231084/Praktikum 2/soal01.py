#Menghitung Body Mass Index
print("Pilih Gender Anda")
print ("1. Pria")
print("2. Wanita")
gender = int(input("= "))
if gender != 1 and gender != 2:
    print('Pilihan tidak valid')
    exit()

TB = float(input("Masukkan tinggi badan (cm) : "))
BB = float(input("Masukkan berat badan (kg) : "))
BMI = BB / ((TB/100) ** 2)

if gender == 1:
    if BMI < 18:
        tipe = "Underweight"
    elif 18 <= BMI < 24:
        tipe = "Normal"
    elif 24 <= BMI < 27:
        tipe = "Overweight"
    elif BMI >= 27:
        tipe = "Obese"
elif gender == 2:
    if BMI < 17:
        tipe = "Underweight"
    elif 17 <= BMI < 24:
        tipe = "Normal"
    elif 24 <= BMI < 28:
        tipe = "Overweight"
    elif BMI >= 28:
        tipe = "Obese"

print(f"Anda tergolong {tipe} dengan BMI {BMI:.2f}")