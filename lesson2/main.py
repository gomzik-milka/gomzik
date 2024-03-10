from character import Character


player1 = Character('Vasya')
player1.show_info()
player2 = Character('Petya', damage=50)
print(player2)

while True:
    if player1.is_alive() and player2.is_alive():
        p1_damage = player1.attack(player2)
        p2_damage = player2.attack(player1)
        print(f'{player2.name} attack {player1.name} '
              f'1 наніс {p2_damage} шкоди')
        print(f'{player1.name} attack {player2.name} '
              f'1 наніс {p1_damage} шкоди')
        print(player2, player1, sep='\n')
    else:
        break

