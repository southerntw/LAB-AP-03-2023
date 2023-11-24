grades = [100, 100, 90, 40, 80, 100, 85, 70.5, 90, 65, 90, 85.5]

grades_total = 0
for i in grades :
    grades_total += i

grades_length = float(len(grades))

average = grades_total / grades_length

summation = 0
for i in grades :
    add = (i - average)** 2
    summation += add
grades_variance = summation/grades_length
print(f"nilai rata-rata:{average :.2f}")
print('jumlah siswa:', grades_length)
print(f"nilai varians:{grades_variance :.2f}")



