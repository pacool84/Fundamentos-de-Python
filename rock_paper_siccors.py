import random

options = ("piedra", "papel", "tijera")

rounds = 1
computer_wins = 0
user_wins = 0

while True:
    
    print('*' * 10)
    print('Round =>', rounds)
    print('*' * 10)

    print('Score Comuptadora ==>', computer_wins)
    print('Score User => ', user_wins)

    user_option = input("piedra, papel o tijera => ")
    user_option = user_option.lower()
    
    rounds += 1

    if not user_option in options:
        print("Esa opcion no es valida")
        continue

    computer_option = random.choice(options) #Nos ayuda a elegir un valor al azar dentro de la tupla options

    print('user option => ', user_option)
    print('computer option => ', computer_option)

    if user_option == computer_option:
        print('Empate')
    elif user_option == "piedra":
        if computer_option == "tijera":
            print('Piedra gana a tijera')
            print('Usuario gano!')
            user_wins += 1
        else:
            print('papel gana a piedra')
            print('Computador gano')
            computer_wins += 1

    elif user_option == "papel":
        if computer_option == "piedra":
            print('papel gana a piedra')
            print('usuario gano')
            user_wins += 1
        else:
            print('tijera gana papel')
            print('Computador gano')
            computer_wins += 1

    elif user_option =='tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')
            print('Usuario gano')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('Computador gano')
            computer_wins += 1
    if computer_wins == 2:
        print('El GANADOR de este juego es la Computadora')
        break
    elif user_wins == 2:
        print('El GANADOR de este juego es el Usuario')
        break
    
    