## Encapsulation, inheritance, abstract class, polymorphism
class Mobil:
    def __init__(self, merek, mesin, silinder):
        self._merek = merek
        self._mesin = mesin
        self._silinder = silinder

    def get_merek(self):
        return self._merek

    def get_mesin(self):
        return self._mesin

    def get_silinder(self):
        return self._silinder
    
    def suara(self):
        return None

class Yamaha(Mobil):
    def info(self):
        return f"Mobil {self._merek} dengan mesin {self._mesin} dan {self._silinder} silinder"
    
    def suara(self):
        return "Broom"

class Honda(Mobil):
    def info(self):
        return f"Mobil {self._merek} dengan mesin {self._mesin} dan {self._silinder} silinder"
    
    def suara(self):
        return "BromBromBrom"

# Polymorphism
def tampilkan_info(motor):
    print(motor.info())

mobil1 = Honda ("HONDA", "1500cc", 2)
mobil2 = Yamaha ("YAMAHA", "1200cc", 4)

tampilkan_info(mobil1)  
tampilkan_info(mobil2)  
print(mobil1.suara())
print(mobil2.suara())