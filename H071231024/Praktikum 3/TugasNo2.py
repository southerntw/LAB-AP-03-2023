print(
    "\nProgram Menghitung Kembalian Dari Suatu Transaksi\n=================================================\n"
)

hB = int(input("Masukkan Harga Barang : "))
nU = int(input("Masukkan Nilai Uang Yang Dibayarkan  : "))


kembalian = nU - hB


pecahanUang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

# Menyimpan Pecahan Uang
jumlahPecahan = {}

# Menghitung Jumlah Pecahan Uang
for pecahan in pecahanUang:
    jumlah = kembalian // pecahan
    if jumlah > 0:
        jumlahPecahan[pecahan] = jumlah
        kembalian -= jumlah * pecahan

# Menghitung Kembalian Dalam Bentuk Pecahan Yang Sesuai
for pecahan in pecahanUang:
    if pecahan in jumlahPecahan:
        print(f"{jumlahPecahan[pecahan]} Uang Sejumlah Rp.{pecahan}")
    else:
        print(f"0 Uang Sejumlah Rp.{pecahan}")
