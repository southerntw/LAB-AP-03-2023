jdl = '\nProgram Mengkonversi Waktu'
grs = '=========================='
print(f'{jdl}\n{grs}\n')

sec = int(input('Konversi Detik ke Jam!\nMasukkan Detik : '))

hour = sec // 3600
sec_sisa = sec % 3600
min = sec_sisa // 60
sec_sisa = sec_sisa % 60

hour_str = str(hour).zfill(2)
min_str = str(min).zfill(2)
sec_str = str(sec_sisa).zfill(2)

print(f'Hasil Konversi : {hour_str} : {min_str} : {sec_str}')       # Jam : Menit : Detik
