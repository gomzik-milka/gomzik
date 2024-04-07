class Action:
    name = 'Kate'
    mood = 60
    health = 100
    money = 0

    def __init__(self, name, health=100, mood=60, money=0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money
