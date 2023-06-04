data = [1,2,3,4]
print(data)

#Concepto de leer datos
print(data[1]) 

#Concepto de actualizar datos
data[-1] = 39
data[0] = 32
print(data)

#Utilizando metodos 

data.append(4) #Por defecto lo agrega en la ultima posicion de las listas
data.insert(0, "Sebastian") #recibe dos parametros, la posicion y el nvo valor 
data.insert(4, "Brenda")
print(data)


#Fusionando o uniendo listas

numbers = [1,2,3,4]
names = ['Sebastian', 'Brenda', 'Paco']

new_list =  numbers + names
print(new_list)


#Identificar en que posicion esta un dato dentro de la lista

search_index = new_list.index("Sebastian")
print(search_index)


#Concepto de eliminar datos

new_list.remove("Brenda")
print(new_list)

new_list.pop() #Este metodo elimina el ultimo dato de la tabla
print(new_list)
new_list.pop(4) #Sin embargo tambien podemos pasar una posicion para ser eliminada 
print(new_list)


#Concepto para invertir las posiciones de una lista 

new_list.reverse()
print(new_list)


#Metodo para ordenar listas
#Considerar que este petodo no funciona cuando en una lista existen diferentes tipos de datos

more_numbers = [3,5,2,1,4]
more_numbers.sort()
print(more_numbers)

more_names = ["Carlos", "Tamara", "Santiago", "Sara", "Paco", "Brenda", "Sebastian"] 
more_names.sort()
print(more_names)
