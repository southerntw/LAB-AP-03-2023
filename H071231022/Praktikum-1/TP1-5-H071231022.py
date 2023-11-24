detik = int(input("masukan detik = "))

jam = detik// 3600 #biar hasilnya bulat
sisa_detik = detik % 3600 #hasil sisa di bagi
menit = sisa_detik // 60
detik = sisa_detik % 60

print(f"{jam:02}:{menit:02}:{detik:02}")
