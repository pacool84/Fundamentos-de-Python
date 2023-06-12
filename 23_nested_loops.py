matrix = [
    [1,2,3],[4,5,6],[7,8,9]
]

print(matrix[0]) #Imprime la posicion 0 de la lista 

#Utilizando el concepto de coordenadas

print(matrix[0][1]) #imprimiria el numero 2
print(matrix[1][0]) #imprimiria el numero 4
print(matrix[2][0]) #imprimiria el numero 7

for row in matrix:
    print(row)
    for column in row:
        print(column)