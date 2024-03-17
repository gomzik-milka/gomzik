class Vampire:
    name = ''
    health = 100
    damage = 1
    defense = 0

    def __init__(self, name, health=100, damage=1, defence=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.defense = defence

    def show_info(self):
        print(self.__str__())

    def __str__(self):
        return f' = {self.name} =\n' \
               f' Health: {self.health}\n' \
               f' Damage: {self.damage}\n' \
               f' Defence: {self.defense}\n'
    def take_damage(self, damage):
        self.health -= damage
        return damage

    def attack(self, target):
        self.health += 6
        return target.take_damage(self.damage)
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False