while True:
    try:
        # Input nilai derajat
        derajat = float(input())
        
        if derajat >= 0 and derajat < 360:
            if (derajat > 270):
                derajat -= 360
            
            # Menghitung jam dari derajat
            jam = 6 + derajat/360 * 24

            print(jam)
            
            # Menentukan waktu berdasarkan jam
            if jam >= 0 and jam < 6:
                waktu = "Selamat Malam"
            elif jam >= 6 and jam < 12:
                waktu = "Selamat Pagi"
            elif jam >= 12 and jam < 18:
                waktu = "Selamat Siang"
            elif jam >= 18 and jam <= 24:
                waktu = "Selamat malam"
            else:
                waktu = "Selamat Sore"

            # Menghitung menit dan detik
            sisa_jam = jam % 1
            menit = int(sisa_jam * 60)
            detik = int((sisa_jam * 60 - menit) * 60)
            jam = int(jam)


            # Menampilkan hasil dalam format yang diinginkan
            print(waktu)
            print(f"{jam:02d}:{menit:02d}:{detik:02d}")

    except ValueError:
        print('data tidak valid')
        break
  
     
