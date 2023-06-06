#Las tuplas son Inmutables
numbers = (1,2,3,4,5)
strings = ("Sebastian", "Brenda", "Paco")
print(numbers)
print(strings)
print(type(numbers))
print(type(strings))

#Accediendo a un dato de la tupla

print(numbers[0])
print(numbers[-1])

print(strings[0])
print(strings[-1])

#En las tuplas no podremos insertar o actualizar mas elementos, Son solo de lectura

#Metodos de las tuplas 

#Metodo INDEX, nos permite identificar la posicion donde se localiza un dato

print(strings.index("Paco"))
print(strings.index("Brenda"))
print(strings.index("Sebastian"))

#Metodo COUNT, cuenta las veces que esta un dato en la tupla 

new_names = ("Sebastian", "Brenda", "Paco", "Sebastian")
print(new_names.count("Sebastian")) #El resultado sera 2

#Tranformacion de Tuplas y Listas utilizando el metodo LIST

my_list = list(new_names)
print(my_list)
print(type(my_list))

#Tranformacion de Listas a Tuplas utilizando el metodo TUPLE

transform_to_tuples = tuple(my_list)
print(transform_to_tuples)
print(type(transform_to_tuples))