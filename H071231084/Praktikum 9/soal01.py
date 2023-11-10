class Human:
    def __init__(self, nama, posisi): #Dipanggil otomatis untuk inisialisasi instance baru 
        self.nama = nama
        self.__posisi = posisi 
        self._speed = 0

    def movement(self, arah): 
        if arah == "L":
            self.__posisi -= self._speed
        elif arah == "R":
            self.__posisi += self._speed

    def get_posisi(self): #memanggil posisinya
        return self.__posisi

class Hero(Human): #mewarisi
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi) #untuk mengambil yg ada di human
        # memberi nilai sesuai soal       
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target): 
        target._health -= self._power

    def get_power(self): #memanggil power
        return self._power
    def set_power(self, power): #mengubah power
        self._power = power

    def get_speed(self):
        return self._speed
    def set_speed(self, speed):
        self._speed = speed

    def get_health(self):
        return self._health
    def set_health(self, health):
        self._health = health

    def get_armor(self):
        return self._armor
    def set_armor(self, armor):
        self._armor = armor

class Warrior(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 26
        self._armor = 30

    def special(self, target):
        self.set_armor(45)
        self.set_power(32)
        target.health -= self._power

class Assassin(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._power = 35
        self.speed = 4

    def special(self, target):
        self.speed = 7
        self.set_power(42)
        target.health -= self._power

class Support(Hero):
    def __init__(self, nama, posisi):
        super().__init__(nama, posisi)
        self._health = 500
        self._armor = 8
        self.speed = 4

    def special(self, target):
        self.speed = 6
        target._health += 150

# Contoh penggunaan
warrior = Warrior("Eren", posisi=10)
assassin = Assassin("Mikasa", posisi=25)
support = Support("Armin", posisi=30)

# Sebelum
print("Health (before):", warrior.get_health())

assassin.attack(warrior)
# Sesudah
print("Health (after) :", warrior.get_health())
print("-" * 10)

# Sebelum
print("Warrior (health):", warrior.get_health())
print("Support (speed) :", support.speed)

support.special(warrior)

# Sesudah
print("Warrior (health):", warrior.get_health())
print("Support (speed) :", support.speed)

print(f'Posisi awal {assassin.nama}: {assassin.get_posisi()}')
assassin.movement("L")
print(f'Posisi {assassin.nama} sekarang: {assassin.get_posisi()}')