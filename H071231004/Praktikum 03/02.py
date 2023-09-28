hargabarang = int(input('Masukkan Harga Barang: '))
uang = int(input('Masukkan Berapa Uang Anda: '))
kembalian = uang - hargabarang

if kembalian < 0: 
    print('Uang Anda Kurang!')
else: 
    pecahan = (100000, 50000, 20000, 10000, 5000, 2000, 1000)
    for i in range(0,7): #akan diulang sebanyak berapa yang epecahan yang ada didalam index 
        jumlah = kembalian // (pecahan[i]) #jumlah lembar uangnya 
        kembalian = kembalian - jumlah * (pecahan[i])
        print(f'{jumlah} Jumlah uang bernilai Rp.{pecahan[i]}') # i = index, yang akan berulang masuk ke index 50k dst 