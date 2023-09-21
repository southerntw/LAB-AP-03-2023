# konversi detik jam

detik = int(input('masukkan jumlah detik = '))


jam = detik // 3600
menit = (detik % 3600) // 60
detik = (detik % 3600) % 60

print(f'{jam:02d}: {menit:02d}: {detik:02d}')