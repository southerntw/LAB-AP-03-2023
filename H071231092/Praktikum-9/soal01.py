class Human:
    def __init__(self, name, pos_x):
        self.name = name
        self._speed = 0
        self.__posisi = pos_x

    def movement(self, arah):
        if arah == "L":
            self.__posisi -= self._speed
        elif arah == "R":
            self.__posisi += self._speed

    def get_posisi(self):
        return self.__posisi
    
    # def set_posisi(self, pos_x):
    #     self.__posisi = pos_x


class Hero(Human):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 15
        self._health = 400
        self._armor = 15
        self._speed = 3

    def attack(self, target):
        target.set_health(target.get_health() - self._power)

    # Getter dan Setter untuk attribut power
    def get_power(self):
        return self._power
    
    def set_power(self, power=15):
        self._power = power
        
    # Getter dan Setter untuk attribut health
    def get_health(self):
        return self._health
    
    def set_health(self, health=400):
        self._health = health
        
    # Getter dan Setter untuk attribut armor
    def get_armor(self):
        return self._armor
    
    def set_armor(self, armor=15):
        self._armor = armor
        
    # Getter dan Setter untuk attribut speed
    def get_speed(self):
        return self._speed
    
    def set_speed(self, speed=3):
        self._speed = speed


class Warrior(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 26
        self._armor = 30
        
    def special(self, target):
        self.set_armor(45)
        self.set_power(32)
        target.set_health(target.get_health() - self._power)
 

class Assassin(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._power = 35
        self.set_speed(4)
        
    def special(self, target):
        self.set_speed(7)
        self.set_power(42)
        target.set_health(target.get_health() - self._power)    


class Support(Hero):
    def __init__(self, name, pos_x):
        super().__init__(name, pos_x)
        self._health = 500
        self._armor = 8
        self.set_speed(4)

    def special(self, target):
        self.set_speed(6)
        target.set_health(target.get_health() + 150)

# Contoh penggunaan
warrior = Warrior("bambang", pos_x=10)
assassin = Assassin("joko", pos_x=25)
support = Support("udin", pos_x=30)

# # Sebelum
# print("Health (before)", warrior.get_health())
# assassin.attack(warrior)
# # Sesudah
# print("Health (after)", warrior.get_health())
# print("-" * 10)

# # Sebelum
# print("Power (Before)", assassin.get_power())
# print("Speed (Before)", assassin.get_speed())
# print("Health (before)", warrior.get_health())
# assassin.special(warrior)
# # Setelah
# print("Power (Setelah)", assassin.get_power())
# print("Speed (Setelah)", assassin.get_speed())
# print("Health (after)", warrior.get_health())
# print("-" * 10)

# # Sebelum
# print("Warrior (health)", warrior.get_health())
# print("Support (speed):", support.get_speed())
# support.special(warrior)
# # Sesudah
# print("Warrior (health)", warrior.get_health())
# print("Support (speed):", support.get_speed())

# print(warrior.get_posisi())