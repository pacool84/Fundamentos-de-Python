'''En este desafío, se te proporcionará una lista de letras llamada letters. 

Tu reto es realizar las siguientes operaciones en orden:

Agregar la letra G al final de la lista.
Reemplazar la letra en la posición 0 con la letra Z.
Eliminar la letra C de la lista.
Imprimir la lista resultante al revés.'''

letters = ['A', 'B', 'C', 'D', 'E', 'F']

letters.append("G")
letters[0] = "Z"
letters.remove("C")
letters.reverse()
print(letters)

