#La sintaxis de un ciclo while es:

""" while True:
    print('Siempre se ejecuta') """


#Ejecutando un contador 
counter = 0

while counter < 10:
    counter += 1
    print(counter)


#Detener un ciclo en algun punto deseado
counter = 0

while counter < 20:
    counter += 1
    if counter == 15:
        break #Forma forzada para romper un ciclo 
    print(counter)


#Otra forma para detener un ciclo 

counter = 0

while counter < 20:
    counter += 1
    if counter < 15:
        continue #Salta automaticamente a la siguiente iteracion del ciclo WHILE
    print(counter)
    print('Este print nunca se ejecutara')