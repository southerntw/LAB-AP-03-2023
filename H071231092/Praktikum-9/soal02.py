class Mahasiswa:
    def __init__(self, Nama, Nim, Jurusan, Ipk):
        self.Nama = Nama
        self.Nim = Nim
        self.Jurusan = Jurusan
        self.Ipk = Ipk
        
    def Tampilkan_info(self):
        print(f"Nama : {self.Nama}\nNim : {self.Nim}\nJurusan {self.Jurusan}\nIpk : {self.Ipk}")
        
    def hitung_predikat(self):
        if self.Ipk >= 3.5 :
            print("“Cumlaude”")
        elif self.Ipk >= 3.0 :
            print("“Sangat Memuaskan”")
        elif self.Ipk >= 2.5 :
            print("“Memuaskan”")
        elif self.Ipk >= 2.0 :
            print("“Cukup”")
        elif self.Ipk < 2.0 :
            print("“Kurang”")
        
mahasiswa = Mahasiswa("Nafil", "H071231092", "Sistem Informasi", 3.5)
mahasiswa.Tampilkan_info()
mahasiswa.hitung_predikat()