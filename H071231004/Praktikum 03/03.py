while True:
    try:
        derajat = float(input("Masukkan derajat = "))
        total_detik = int(derajat * 240 + 21600) % 86400
        #240 itu detik yang sama dengan 1 derajat 
        #21600 itu sama dengan 6 jam 
        #86400 itu sama dengan jumlah detik dalam sehari full (24 jam)
        #cari sisa hadi baginya karena formatnya 24 jam 
        jam = total_detik // 3600
        sisa = total_detik % 3600
        menit = sisa // 60
        detik = sisa % 60

        if 6 <= jam < 12:
            waktu = "Pagi"
        elif 12 <= jam < 15:
            waktu = "Siang"
        elif 15 <= jam < 18:
            waktu = "Sore"
        else:
            waktu = "Malam"

        print(f"Selamat {waktu}\n{jam:02}:{menit:02}:{detik:02}")
    except ValueError:
        print("End of File")
        break
