# Input detik yg diinginkan
print("Konversi detik ke jam")
detik = int(input("Masukkan jumlah detik : "))

# Rumus detik ke jam, menit dan detik
jam = detik // 3600
menit = (detik % 3600) // 60
detik = detik % 60

# Output hasil
print(f'{jam:02d}:{menit:02d}:{detik:02d}')