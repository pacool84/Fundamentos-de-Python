#Sintaxis basica de un FOR

for element in range(1, 21):
    print(element)

#Iterando sobre una lista
my_list = [33, 35, 45, 56, 'Sebastian', 'Brenda', 'Paco']

for i in my_list:
    print('Iterando sobre la lista',i)

#Iterando sobre una tupla

my_tuple = ('Paco', 'Natalia','Tamara', 'Paulina', 'Paco jr')

for i in my_tuple:
    print('Iterando sobre la tupla',i)

#Iterando sobre un diccionario 

my_dictionary = {
    'name': 'camisa',
    'price': 100,
    'stock': 39
}

for i in my_dictionary: #Al iterar sobre un diccionario los resultados sobre los que itera son los KEY / llaves
    print('Iterando sobre el diccionario', i)

#Si necesitaramos los valores se realiza de la siguiente manera:

for i in my_dictionary:
    print('Iterando sobre los VALUES del diccionario', my_dictionary[i])

#Existe una forma mas sencilla para obtener el KEY y VALUE de un diccionario 

for key, value in my_dictionary.items():
    print(key, '==>', value)

#Ejemplo de una lista de diccionario - mas apegado a la vida real 

people = [
    {
        'name': 'Sebastian',
        'age': 8
    },
    {
        'name': 'Brenda',
        'age': 33
    },
    {
        'name': 'Paco',
        'age': 39
    }
]

for person in people:
    print(person['name'])
    print(person['age'])