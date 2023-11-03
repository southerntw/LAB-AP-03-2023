import os,random,time

# Fungsi untuk membuat ID transaksi
def membuat_transaksi_id():
    waktu_sekarang = time.localtime()
    nomor_acak= random.randint(100, 999)
    transaksi_id = nama_kasir[:1].upper() + time.strftime("%y%m%d%H%M%S", waktu_sekarang) + str(nomor_acak)
    return transaksi_id

# Fungsi untuk mencetak invoice
def print_invoice(transaksi_id, nama_kasir, products):
    invoice_filename = f"\Python\Tugas Pratikum\TUGAS 07\invoices\{transaksi_id}.txt"
    
    with open(invoice_filename, "w") as invoice_file:
        total_price = 0

        invoice_file.write("\n{:>37.5} {:<37.5}\n\n".format("TOKO", nama_kasir.upper()))
        invoice_file.write(f"{'='*75}\n")
        invoice_file.write(f"Kasir: {nama_kasir}\n")
        invoice_file.write(f"Waktu Transaksi: {time.strftime('%d/%m/%y  %H:%M')}\n")
        invoice_file.write(f"{'='*75}\n\n")
        invoice_file.write("{:^65}\n".format("Daftar Produk"))
        invoice_file.write(f"{' '*5}{'='*60}\n")
        invoice_file.write("{}|{:^14}|{:^14}|{:^8}|{:^19}|\n".format(' '*5, "Nama","Harga","Jumlah","Total"))
        invoice_file.write(f"{' '*5}{'='*60}\n")
        for product in products:
            nama_produk, harga, jumlah = product
            total_product_price = harga * jumlah
            total_price += total_product_price
            invoice_file.write("{}|{:<14}|{:>14}|{:^8}|{:>19}|\n".format(' '*5, nama_produk, 'Rp.'+str(harga), jumlah, 'Rp.'+str(total_product_price)))
        
        invoice_file.write(f"{' '*5}{'='*60}\n")
        invoice_file.write("{}|{:^38}|{:>19}|\n".format(" "*5, "TOTAL", 'Rp.'+str(total_price)))
        invoice_file.write(f"{' '*5}{'='*60}\n\n")
        invoice_file.write(f"{'='*75}\n")
        invoice_file.write("{:^75}\n".format("Terimaksih Telah Belanja"))
        invoice_file.write(f"{'='*75}\n")


# Fungsi untuk mencari dan menampilkan invoice berdasarkan ID transaksi
def search_invoice_by_id():
    mencari_transaksi_id = input("Masukkan ID Transaksi : ")
    print("="*50)
    file_read = f"\Python\Tugas Pratikum\TUGAS 07\invoices\{mencari_transaksi_id}.txt"
    if not os.path.exists(file_read):
        print(f"Invoice dengan ID {mencari_transaksi_id} tidak ditemukan.")
        print("="*50)
    else:
        with open(file_read, "r") as invoice_file:
            content = invoice_file.read()
            print(content)
            print("="*50)

# Fungsi untuk menyimpan riwayat transaksi
def menyimpan_transaksi_history(transaksi_id, total_price):
    invoice_filename = f"\Python\Tugas Pratikum\TUGAS 07\invoices/try_history.txt"
    if not os.path.exists(invoice_filename) :
        with open(invoice_filename, "a") as history_file:
            history_file.write(f"{'='*75}\n")
            history_file.write("|{:^73}|\n".format("RIWAYAT TRANSAKSI"))
            history_file.write(f"{'='*75}\n")
            history_file.write("|{:^19}|{:^26}|{:^26}|\n".format("Waktu", "ID Transaksi", "Nominal Transaksi"))
            history_file.write(f"{'='*75}\n")
    
    with open(invoice_filename, "a") as history_file:
        current_time = time.strftime("%Y/%m/%d %H:%M", time.localtime())
        history_file.write("|{:^19}|{:<26}|{:>26}|\n".format(current_time, transaksi_id, "Rp."+str(total_price)))
        history_file.write(f"{'='*75}\n")


# Membuat folder "invoices" jika belum ada
folder_path = "\Python\Tugas Pratikum\TUGAS 07\invoices"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


print("="*50)
print("{:^50}".format("SELAMAT DATANG"))
print("="*50)
nama_kasir = input("Masukkan nama kasir   : ")

while True:
    print("="*50)
    print("Pilih opsi:")
    print("1. Transaksi Baru")
    print("2. Cari Invoice")
    print("3. Keluar")
    print("="*50)
    pilihan = input("Pilih menu (1-3): ")
    print("="*50)

    if pilihan == "1":
        # Inisialisasi list produk
        products = []

        while True:
            nama_produk = input("Masukkan nama produk: ")
            while True:
                try:
                    harga = int(input("Harga produk: "))
                    break
                except ValueError:
                    print("Harga Produk harus angka. Silahkan coba lagi")
            while True:
                try:
                    jumlah = int(input("Jumlah produk yang akan dibeli: "))
                    break
                except ValueError:
                    print("Jumlah Produk harus angka. Silahkan coba lagi")
            products.append((nama_produk, harga, jumlah))
            print("="*50)
            pilihan2 = input("Tambah Prooduk? (y/t) : ")
            print("="*50)
            if pilihan2 == "y":
                continue
            elif pilihan2 == "t":
                # Membuat ID transaksi
                transaksi_id = membuat_transaksi_id()

                # Mencetak invoice
                print_invoice(transaksi_id, nama_kasir, products)

                total_price = sum(harga * jumlah for _, harga, jumlah in products)
                menyimpan_transaksi_history(transaksi_id, total_price)

                print("{:^50}".format("TRANSAKSI BERHASIL"))
                break

    elif pilihan == "2":
        # Meminta ID transaksi
        search_invoice_by_id()

    elif pilihan == "3":
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")