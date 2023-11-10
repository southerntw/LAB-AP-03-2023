class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    def tampilkan_info(self):
        print('Nama\t: ', self.nama)
        print('NIM\t: ', self.nim)
        print('Jurusan\t: ', self.jurusan)
        print('IPK\t: ', self.ipk)

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Cukup"
        elif self.ipk < 2.0:
            return "Kurang"
        
mahasiswa1 = Mahasiswa("Khalika", "H071231084", "Sistem Informasi", 4.00)
mahasiswa1.tampilkan_info()
print("Predikat: ", mahasiswa1.hitung_predikat())