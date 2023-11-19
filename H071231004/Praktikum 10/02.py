from abc import ABC, abstractmethod
# kelas parents 
class Hewan(ABC):
    def __init__(self, nama):
        self._nama = nama

    @abstractmethod
    def bersuara(self):
        pass
# Class anak
class Ular(Hewan):
    def bersuara(self):
        return f"{self._nama} mengeluarkan suara: Ssstttt!"

class Serigala(Hewan):
    def bersuara(self):
        return f"{self._nama} mengeluarkan suara: Auuuu!"

class Dinosaurus:
    def __init__(self, nama):
        self._nama = nama

    def bersuara(self):
        return f"{self._nama} mengeluarkan suara: Rwarrr!"

# memanggil suara dari kelas hewan
def suara_hewan(hewan):
    print(hewan.bersuara())
    
ular1 = Ular("Anaconda")
suara_hewan(ular1)
serigala1 = Serigala("Foxx")
suara_hewan(serigala1)
dinosaurus1 = Dinosaurus("Tirex")
suara_hewan(dinosaurus1)