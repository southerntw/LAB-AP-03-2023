class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    def Tampilkan_info(self):
        return (f"Nama : {self.nama}\nNIM : {self.nim}\nJurusan : {self.jurusan}\nIPK : {self.ipk}")
    def Hitung_Predikat(self):
        if self.ipk >= 3.5:
            return "Cumlaude"
        elif 3.0 <= self.ipk < 3.5:
            return "Sangat Memuaskan"
        elif 2.5 <= self.ipk < 3.0:
            return "Memuaskan"
        elif 2.0 <= self.ipk < 2.5:
            return "Cukup"
        else:
            return "Kurang"
        
mahasiswa1 = Mahasiswa("Syahrini", "H071231066", "Sistem Informasi", 3.4)
mahasiswa2 = Mahasiswa("Fariz", "H071231011", "Teknik", 4.0)
print(mahasiswa1.Hitung_Predikat())
print(mahasiswa1.Tampilkan_info())
print(mahasiswa2.Tampilkan_info())
print(mahasiswa2.Hitung_Predikat())