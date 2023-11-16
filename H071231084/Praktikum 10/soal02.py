class Wizard:
    def __init__(self, name, house):
        self.name = name
        self._house = house
    def get_house(self):
        return self._house
    def set_house(self, house):
        self._house = house
    def cast_spell(self):
        return None

class HarryPotter(Wizard):
    def __init__(self, name, house):
        super().__init__(name, house)
        self.name = "Harry Potter"

    def cast_spell(self):
        return "Expecto Patronum!"

class HermioneGranger(Wizard):
    def __init__(self, name, house):
        super().__init__(name, house)

    def cast_spell(self):
        return "Alohomora!"

class DracoMalfoy(Wizard):
    def __init__(self, name, house):
        super().__init__(name, house)

    def cast_spell(self):
        return "Expelliarmus!"

harry = HarryPotter("Harry Potter", "Gryffindor")
hermione = HermioneGranger("Hermione Granger", "Gryffindor")
draco = DracoMalfoy("Draco Malfoy", "Slytherin")

wizards = [harry, hermione, draco]
for wizard in wizards:
    print(f"{wizard.name} from {wizard.get_house()} house casts spell: {wizard.cast_spell()}")