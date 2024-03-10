from character import Character


player1 = Character('Vasya')
player1.show_info()
player2 = Character('Petya', damage=50)
print(player2)

while True:
    if player1.is_alive() > 0:
        p1_damage = player2.attack(player1)
        print(f'{player2.name} attack {player1.name} '
              f'1 наніс {p1_damage} шкоди')
        print(player2, player1, sep='\n')
