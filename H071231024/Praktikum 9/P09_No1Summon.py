from P09_No1Class import Warrior, Assassin, Support

warrior = Warrior("Zilong", pos_x=10)
assassin = Assassin("Fanny", pos_x=25)
support = Support("Floryn", pos_x=30)

print("=" * 30)
# sebelum
print("Health (Before) :", warrior.get_health())
assassin.attack(warrior)
# sesudah
print("Health (After)  :", warrior.get_health())
print("-" * 30)
# sebelum
print("Warrior (Health):", warrior.get_health())
print("Support (Speed) :", support.get_speed())
support.special(warrior)
print("-" * 30)
# sesudah
print("Warrior (Health):", warrior.get_health())
print("Support (Speed) :", support.get_speed())
print("-" * 30)


support.movement("L")
print(support.get_pos_x())
print("=" * 30)

print("Warrior (Pos) :", warrior.get_pos_x())

warrior.movement("R")
print(warrior.get_pos_x())
