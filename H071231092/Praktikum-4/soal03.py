def MencariMaxAngka(angka):
    # Inisialisasi nilai terbesar dengan angka pertama dalam daftar
    max_angka = angka[0]

    # Loop melalui daftar untuk mencari angka terbesar
    for num in angka:
        if num > max_angka:
            max_angka = num
    
    return max_angka

# Contoh penggunaan fungsi
angka = 1,2,4,6,9,3,1,9,10
hasil = MencariMaxAngka(angka)
print(f"Maksimum {angka}")
print(">>", hasil)