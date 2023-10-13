def buat_string(kata):
    indeks_tengah = len(kata) // 2
    if len(kata) % 2 == 0: #apakah genap?
        middle_char = kata[indeks_tengah - 1] + kata[indeks_tengah]
    else:
        middle_char = kata[indeks_tengah]
    return kata[0] + middle_char + kata[-1]
kata = 'ananta'
print(buat_string(kata)) 