grades = [100, 100, 90, 40, 80, 100, 85, 70.5, 90, 65.5, 90, 85.5]

grades_total = 0
for i in grades:
    grades_total += i

grades_length = int(len(grades))

average = grades_total / grades_length

summation = 0
for score in grades:
    add = (score - average) ** 2
    summation += add
grades_variance = summation / grades_length

print(f"Nilai rata-rata: {average:.2f}")
print(f"Jumlah siswa: {grades_length}")
print(f"Nilai varians: {grades_variance:.2f}")