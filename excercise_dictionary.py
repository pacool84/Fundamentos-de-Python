""" En este desafío, se te proporcionará un diccionario llamado person que contiene información sobre una persona. 
Tu reto es realizar las siguientes operaciones en orden:

Agregar un nuevo elemento al diccionario con la llave "twitter" y el valor "@nicobytes".
Actualizar el valor del elemento con la llave "name" con el valor "Felipe".
Eliminar el elemento del diccionario con la llave "age".
Imprimir una lista con las llaves del diccionario.
Imprimir una lista con los valores del diccionario. """

person = {
    'name': 'Nicolas',
    'lastName': 'Molina',
    'age': 29
}

person['twitter'] = '@nicobytes'
person['name'] = 'Felipe'
person.pop('age')
print(list(person.keys()))
print(list(person.values()))
print(person)