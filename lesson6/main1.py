from main import Person
import random
human = Person(name='Kate', money=50, mood=50, health=100)
human.change_state(
    money=random.randint(50, 100),
    mood=random.randint(-20, -10),
    health=random.randint(-10, -5)
    )
print(human)