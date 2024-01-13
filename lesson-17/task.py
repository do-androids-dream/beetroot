class Location:
    def __init__(self, name, *chars):
        self.name = name
        self.condition = "Normal"
        self.chars = chars

    def destruct(self):
        print(f"{self.name} has been destructed and all the creatures on it has fallen down\n")
        self.condition = "Destroyed"
        for char in self.chars:
            char.fall()


class LotrCharachter:
    def __init__(self, name, special, age, weapon):
        self.name = name
        self.special = special
        self.age = age
        self.weapon = weapon


class Demon(LotrCharachter):
    def __init__(self, name, special, age, weapon):
        super().__init__(name, special, age, weapon)

    def fall(self):
        print(f"{self.name} has fallen\n")
        self.die()

    def die(self):
        print(f"{self.name} has died\n")
        del self


class Wizard(LotrCharachter):
    def __init__(self, name, special, age, weapon):
        super().__init__(name, special, age, weapon)

    def you_shall_not_pass(self, enemy: Demon, location:Location):
        print(
            f"{self.name}: I am a servant of the Secret Fire, wielder of the flame of Anor. "
            f"You cannot pass. The dark fire will not avail you, flame of Udûn. Go back to the Shadow! You cannot pass.\n"
        )
        location.destruct()
        print(f"{self.name} has defeated {enemy.name}")

    def fall(self):
        print(f"{self.name} catch the edge\n")


#######################################################################################


balrog = Demon("Balrog", "fire", None, "whip")
gandalf = Wizard("Gandalf the Grey", "magic", None, "staff")
bridge = Location("Bridge of Khazad-dûm", balrog, gandalf)

gandalf.you_shall_not_pass(balrog, bridge)

