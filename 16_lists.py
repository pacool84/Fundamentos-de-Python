numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers)) #<class 'list'>

#Los datos de tipo lista pueden guardar diferentes tipos de datos

tasks = ['Lavar platos', 'jugar videojuegos', 10, True]
print(tasks)


#Accediendo a las posiciones de las listas 

print(numbers[0])
print(tasks[3])
print(tasks[1])
print(tasks[0:]) #Accediendo a todos los datos de la lista


#Mutacion de listas 

tasks[0] = "estudiar python"
print(tasks)

tasks[2] = 39
print(tasks)

tasks[1] = False
print(tasks)


#Aplicando concepto de Slicing a las listas 

print(len(tasks))
print(tasks[-1])
print(tasks[0:2])


#Utilizando el metodo IN en listas 

print(True in tasks)
print("video" in tasks)
print(39 in tasks)