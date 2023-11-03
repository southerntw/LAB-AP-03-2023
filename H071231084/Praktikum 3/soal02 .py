harga_barang = int(input("Harga barang: "))
uang_dibayarkan = int(input("Uang dibayarkan: "))

kembalian = uang_dibayarkan - harga_barang
if kembalian < 0:
    print("Uang Anda kurang!")
    exit()

pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000]

for pecahan in pecahan_uang:
    jumlah_uang = kembalian // pecahan
    kembalian %= pecahan
    print(f"{jumlah_uang} uang sejumlah Rp, {pecahan:,.0f}".replace(",", "."))