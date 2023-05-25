lives = 3
print(type(lives))

age = 39
budget = 67000

# Float / Flotantes
temperature = 12.12
print(type(temperature))

lives = lives + 10
print(lives)

lives = lives - temperature
print(lives)
print(type(lives))

# Forma facil de operar con sumas y restas en python

lives = 5
lives -= 1
print(lives)
lives -= 2
print(lives)

lives += 2
print(lives)

lives += 1
print(lives)

# Representacion de numeros muy grandes

number_long = 450000000000000000000000000000.1
print(number_long)

number_long = 0.000000000030000000000000000000
print(number_long)


# Ejercicio .- Calcular el promedio de presupuesto para tres meses

january_budget = 300
february_budget = 150
march_budget = 500.10

total_budget = january_budget + february_budget + march_budget
print("El presupuesto total es de $", total_budget)

average_budget = total_budget / 3
print("El promedio de tu presupuesto es de $", average_budget)

# El metodo int nos permite cambiar a un tipo de dato entero
tranform = int(average_budget)
print(type(tranform))
