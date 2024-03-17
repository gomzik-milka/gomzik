from lesson2.character import Character
from vampir import Vampire


player1 = Character('Vasya')
player1.show_info()

player2 = Vampire('Petya', damage=50)
print(player2)

while player1.is_alive() and player2.is_alive():
        p1_damage = player1.attack(player2)
        p2_damage = player2.attack(player1)
        print(f'{player2.name} attack {player1.name} '
              f'1 наніс {p2_damage} шкоди')
        print(f'{player1.name} attack {player2.name} '
              f'1 наніс {p1_damage} шкоди')
        print(player2, player1, sep='\n')

print(player2, player1, sep='\n')
