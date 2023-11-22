from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def HitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    def HitungLuas(self):
        return self.sisi ** 2

class Kendaraan():
    def __init__(self, merk):
        self.__merk = merk  

    def Tampilan(self):
        pass
    
    def get_merk(self):
        return self.__merk

    def set_merk(self, merk):
        self.__merk = merk

class Mobil(Kendaraan):
    def __init__(self, merk, model):
        super().__init__(merk)
        self.__model = model

    def Tampilan(self):
        return (f"Mobil {self.get_merk()} model {self.__model}")

class Motor(Kendaraan):
    def __init__(self, merk, jenis):
        super().__init__(merk)
        self.__jenis = jenis

    def Tampilan(self):
        return (f"Motor {self.get_merk()} jenis {self.__jenis}")

mobil = Mobil("Toyota", "Avanza")
print(mobil.Tampilan())

motor = Motor("Honda", "Sport")
print(motor.Tampilan())

x = Persegi(11)
print(x.HitungLuas())
