while True:
    try:
        sudut = float(input("Masukkan sudut: "))
        
        if not 0 <= sudut <= 360:
            print("Masukkan sudut yang benar!")
            exit()

        jam = int(sudut // 15 + 6) # 15 = 360/24 = sudut/jam
        sisa_sudut = sudut % 15
        menit = int(sisa_sudut // (1/4)) # 1/4 = sudut/menit = (sudut/jam) / 60 menit = 15 / 60 
        sisa_sudut2 = sisa_sudut % (1/4)
        detik = int(sisa_sudut2 // (1/240)) # 1/240 = sudut/detik = (sudut/menit) / 60 detik = (1/4) / 60
        
        if jam >= 24:
            jam -= 24
        
        waktu_asli = "{:02d}:{:02d}:{:02d}".format(jam, menit, detik)
        
        ucapan_waktu = ""
        if jam >= 6 and jam < 12:
            ucapan_waktu = "Selamat Pagi"
        elif jam >= 12 and jam < 15:
            ucapan_waktu = "Selamat Siang"
        elif jam >= 15 and jam < 18:
            ucapan_waktu = "Selamat Sore"
        else:
            ucapan_waktu = "Selamat Malam"
        
        print(ucapan_waktu)
        print(waktu_asli)
    
    except ValueError:
        print("Masukkan nilai yang benar!")
        break