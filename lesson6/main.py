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

human.change_state(
        money=100,
        mood=-50,
        health=-5
    )

