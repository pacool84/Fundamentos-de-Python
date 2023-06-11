persons = {
    'name': "Sebastian",
    'last_name': "Lopez",
    'age': 8,
    'langs': ['javascript', 'python'],
    
}

print(persons)

#Actualizacion a Diccionarios

persons['name'] = 'Paco'
persons['age'] += 31
persons['langs'].append('Servicenow') #Podemos usar append por que el tipo de dato dentro del diccionario es una lista 
print(persons)

#Eliminando datos dentro del diccionario con el metodfo DEL y POP

del persons['last_name']
persons.pop('langs')
print(persons)

#Obteniendo los items de un diccionario
family = {
    'Son': "Sebastian",
    'last_name': 'Lopez',
    'age': 8,
    'Mom': 'Brenda',
    'last_name': 'Rosales',
    'age': 32
    

}
print(family)
print(family.items()) #Regresa el resultado como pares de tuplas
print(family.keys()) #Regresa el resultado con los atributos del diccionario
print(family.values())#Regresa el resultado con los valores del diccionario

