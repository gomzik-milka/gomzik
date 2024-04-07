from main2 import Action
class Person:
    name = 'Kate'
    health = 100
    mood = 50
    money = 50

    def __init__(self, name, health=100, mood=50, money=50):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def show_info(self):
        print(self.__str__())

    def do(self, Action):
        self.health += Action.health
        self.mood += Action.mood
        self.money += Action.money

    def __str__(self):
        return f' = {self.name} =\n' \
               f' Health: {self.health}\n' \
               f' mood: {self.mood}\n' \
               f' money: {self.money}\n'

    def change_state(self, money, mood, health):
        self.money += money
        self.mood += mood
        self.health += health
        if health < 0:
            print('Я померла')
        if mood < 0:
            print('Я впала в діпрессію')
        if money < 0:
            print('Я бомж')

human = Person(name='Kate', money=50, mood=50, health=100)
print(human)
human.change_state(
        money=100,
        mood=-50,
        health=-5
)

print(human)
print('Змінено значення')

human = Person(name='Kate', money=50, mood=50, health=100)

go_to_park = Action(name='Сходити у парк', money=0, mood=15, health=3)
human.do(go_to_park)

print(human)
print('Сходив у парк')

