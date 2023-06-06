import random

options = ("piedra", "papel", "tijera")
user_option = input("piedra, papel o tijera => ")
user_option = user_option.lower()

if not user_option in options:
    print("Esa opcion no es valida")
    
computer_option = random.choice(options)

print('user option => ', user_option)
print('computer option => ', computer_option)

if user_option == computer_option:
    print('Empate')
elif user_option == "piedra":
    if computer_option == "tijera":
        print('Piedra gana a tijera')
        print('Usuario gano!')
    else:
        print('papel gana a piedra')
        print('Computador gano')

elif user_option == "papel":
    if computer_option == "piedra":
      print('papel gana a piedra')
      print('usuario gano')
    else:
        print('tijera gana papel')
        print('Computador gano')

elif user_option =='tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('Usuario gano')
    else:
        print('piedra gana a tijera')
        print('Computador gano')