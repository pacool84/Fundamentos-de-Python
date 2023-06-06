#Los diccionarios funcionan con base a llave / valor - key / value

my_dictionary = {
    'nombre': "Sebastian",
    'apellido': "Lopez",
    "edad": 8
}
print(my_dictionary)
print(type(my_dictionary))

#Para conocer el tamaño de un diccionario 
print(len(my_dictionary))

#Para poder leer datos en un diccionario 

print(my_dictionary["nombre"])
print(my_dictionary["apellido"])
print(my_dictionary["edad"])


#Leyendo datos con el metodo GET, la diferencia de la forma anterior es que podemos manejar situaciones en donde no exista ese valor en el diccionario, retornaria un NONE
#Es mucho mas recomendable utilizar este metodo
print(my_dictionary.get("nombre"))
print(my_dictionary.get("apellido"))
print(my_dictionary.get("años")) #Esta llave no existe en el diccionario de ejemplo

#Saber si una llave exite en un diccionario con el metodo IN

print("nombre" in my_dictionary)
print("edad" in my_dictionary)
print("Brenda" in my_dictionary)