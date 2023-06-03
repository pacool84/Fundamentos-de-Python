user_option = input("piedra, papel o tijera => ")
user_option = user_option.lower()
computer_option = 'papel'

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