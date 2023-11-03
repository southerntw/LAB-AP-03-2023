def hitung_isi(kata):    
    jumlah_a = 0
    jumlah_b = 0
    jumlah_c = 0
    jumlah_lain = 0
    if kata == "":
        print("ERROR: Input tidak boleh kosong!")
    for i in kata:
        if i == "a" or i == "A":
            jumlah_a += 1
        elif i == "b" or i == "B":
            jumlah_b += 1
        elif i == "c" or i == "C":
            jumlah_c += 1
        else:
            jumlah_lain += 1    
    print("Jumlah huruf A:", jumlah_a)
    print("Jumlah huruf B:", jumlah_b)
    print("Jumlah huruf C:", jumlah_c)
    print("Jumlah huruf lain:", jumlah_lain)

while True:
    baris = input('Masukkan huruf: ')
    hitung_isi(baris)