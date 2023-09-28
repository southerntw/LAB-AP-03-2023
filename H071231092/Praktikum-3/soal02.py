# input harga barang dan uang dibayarkan
harga_barang = int(input(''))
uang_dibayarkan = int(input(''))

# Menghitung kembalian
kembalian = uang_dibayarkan - harga_barang

# Daftar pecahan uang
pecahan_uang = [100000,50000,20000,10000,5000,2000,1000]

jumlah_pecahan = {}

# Menghitung jumlah masing-masing pecahan
for pecahan in pecahan_uang:
    if kembalian >= pecahan:
        jumlah = kembalian // pecahan
        jumlah_pecahan[pecahan] = jumlah
        kembalian %= pecahan

for pecahan in pecahan_uang:
    if pecahan in jumlah_pecahan:
        print(f'{jumlah_pecahan[pecahan]} uang sejumlah Rp.{pecahan}')
    else:
        print((f"0 uang sejumlah Rp.{pecahan}"))
