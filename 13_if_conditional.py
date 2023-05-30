# Condicional IF

if True:
    print("Deberia ejecutarse ")

if False:
    print("No debe de ejecutarse ")

pet = input("Cual es tu mascota favorita?")

if pet == "perro":
    print("Tienes un buen gusto")

if pet == "gato":
    print("Que feos gustos tienes ")


# Utilizando el IF ELSE
stock = int(input("Digita el stock =>"))

if stock >= 100 and stock <= 1000:
    print("El stock es correcto")
else:
    print("El stock es incorrecto ")

# Utilizando el ELSEIF

pokemon = input("Cual es tu pokemon favorito =>")

if pokemon == "pikachu":
    print("Eres un gran maestro pokemon")
elif pokemon == "charizard":
    print("Eres una leyenda")
elif pokemon == "cocofuego":
    print("Eres un maestro noob")
else:
    print("No te deberias de considerar un maestro pokemon ")

# Ejercicio, crear un programa para evaluar si un numero es par o impar

numero = int(input("Digita un numero entre el 0 y infinito ==> "))


if numero % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
