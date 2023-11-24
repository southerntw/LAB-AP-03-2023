class Human:
    def __init__(self, name, position):
        self.name = name  # public attribute
        self._speed = 0
        self.__position = position  # private attribute

    def movement(self, direction):
        if direction == 'L':
            self.__position -= self._speed
        elif direction == 'R':
            self.__position += self._speed

    def set_position(self, value):
        self.__position = value

    def get_position(self):
        return self.__position

    def set_speed(self, value):
        self._speed = value

    def get_speed(self):
        return self._speed


class Hero(Human):
    def __init__(self, name, position, power, health, armor, speed):
        super().__init__(name, position)
        self._power = power  # protected attribute
        self._health = health  # protected attribute
        self._armor = armor  # protected attribute
        self._speed = speed  # protected attribute

    def attack(self, target):
        target.set_health(target.get_health() - self._power)

    def set_health(self, value):
        self._health = value

    def get_health(self):
        return self._health

    def set_power(self, value):
        self._power = value

    def get_power(self):
        return self._power

    def set_armor(self, value):
        self._armor = value

    def get_armor(self):
        return self._armor


class Warrior(Hero):
    def __init__(self, name, position):
        super().__init__(name, position, power=26, health=400, armor=30, speed=3)

    def special(self, target):
        target.set_armor(target.get_armor() - 45)
        target.set_power(target.get_power() - 32)


class Assassin(Hero):
    def __init__(self, name, position):
        super().__init__(name, position, power=35, health=400, armor=15, speed=4)

    def special(self, target):
        self.set_speed(self.get_speed() + 7)
        target.set_health(target.get_health() - self.get_power())


class Support(Human):
    def __init__(self, name, position):
        super().__init__(name, position)
        self._health = 500  # protected attribute
        self._armor = 8  # protected attribute
        self._speed = 4  # protected attribute

    def special(self, target):
        self.set_speed(self.get_speed() + 6)
        target.set_health(target.get_health() + 150)

    def set_health(self, value):
        self._health = value

    def get_health(self):
        return self._health

    def set_armor(self, value):
        self._armor = value

    def get_armor(self):
        return self._armor

# if __name__ == "__main__":
warrior = Warrior("Bambang", position=10)
assassin = Assassin("Joko", position=25)
support = Support("Udin", position=30)

# sebelum
print("health (before)", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("health (after)", warrior.get_health())

print("-" * 10)


print("Warrior (health)", warrior.get_health())
print("Support (speed)", support.get_speed())

support.special(warrior)
# sesudah
print("Warrior (health)", warrior.get_health())
print("Support (speed)", support.get_speed())

print  (assassin.name)
# print ('selamat pagi,andi')