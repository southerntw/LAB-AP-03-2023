class Mahasiswa:
    def __init__(self, nama, nim, jurusan, ipk):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk
    def tampilkan_info(self):
        return (f"Nama : {self.nama}\nNIM : {self.nim}\nJurusan : {self.jurusan}\nIPK : {self.ipk}")
    def hitung_predikat(self):
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
        
mahasiswa1 = Mahasiswa("Syahrini", "H071231066", "Teknik", 3.4)
mahasiswa2 = Mahasiswa("Nancy", "H071231004", "Sistem Informasi", 4.0)
print(mahasiswa1.hitung_predikat())
print(mahasiswa2.tampilkan_info())