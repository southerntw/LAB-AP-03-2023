print('Menghitung Body Mass Indeks (BMI)')

print('Pilih Gender Anda: \n 1. Laki \n 2. Perempuan')
g = input('= ')

bb = int(input('Masukkan berat badan (kg) : '))
tb = int(input('Masukkan tinggi badan (cm) : '))

# Konversi tinggi badan ke meter
tb = tb/100

# Rumus BMI = berat badan(kg) / (tinggi badan(m) ^ 2)
bmi = (bb / (tb**2))

print('Nilai BMI anda = {:.2f}'.format(bmi))

if g := 1:
    if bmi <= 18: 
        print('Anda tergolong underwight dengan BMI {:.2f}'.format(bmi))
    elif bmi >= 18 and bmi <= 23.9:
        print('Anda tergolong normal dengan BMI {:.2f}'.format(bmi))
    elif bmi >= 24 and bmi <= 26.9:
        print('Anda tergolong overweight dengan BMI {:.2f}'.format(bmi))
    else:
        print('Anda tergolong obese dengan BMI {:.2f}'.format(bmi))
elif g == 2:
    if bmi <= 17:
        print('Anda tergolong underweight dengan BMI {:.2f}'.format(bmi))
    elif bmi >= 17 and bmi <= 23.9:
        print('Anda tergolong normal dengan BMI {:.2f}'.format(bmi))
    elif bmi >= 24 and bmi <= 27.9:
        print('Anda tergolong overweight dengan BMI {:.2f}'.format(bmi))
    else: 
        print('Anda tergolong obese dengan BMI {:.2f}'.format(bmi))
else:
    print('Jenis kelamin tidak valid')