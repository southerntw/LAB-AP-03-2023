def hitung_isi(kata):
    jumlah_a = 0
    jumlah_b = 0
    jumlah_c = 0
    jumlah_lain = 0
    if kata == '':
        print('ERROR: Input tidak boleh kosong!')
    for i in kata:
        if i == 'a':
            jumlah_a += 1
        elif i == 'b':
            jumlah_b += 1
        elif i == 'c':
            jumlah_c += 1
        else:
            jumlah_lain += 1 
    print('jumlah huruf A: ', jumlah_a)
    print('jumlah huruf B: ', jumlah_b)
    print('jumlah huruf C: ', jumlah_c)
    print('jumlah karakter lain: ', jumlah_lain)
while True:
    baris = input('Masukkan huruf: ')
    hitung_isi(baris)