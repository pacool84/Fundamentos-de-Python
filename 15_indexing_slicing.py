#INDEXING
#Los textos tienen un indicador en donde se puede ingresar a nivel de posición 
text = "Sebas sabe programar en Python"


print(text[0]) #Retornaria la S
print(text[1]) #Retornaria la e

#En caso de que quisieramos acceder a una posicion que no existe Python enviara el mensaje de error IndexError: string index out of range
#print(text[999])

#Ejercicio: Accede a la ultima posicion del texto definido
last_position = len(text) - 1 
print(text[last_position])

#Python cuenta con diversas funcionalidades y pudieramos ingresar a la ultima posicion de la siguiente forma
print(text[-1])


#SLICING
print(text[0:5]) #Considerar una posicion mas hacia adelante ya que no toma en cuenta este metodo la ultima posicion referenciada

#Otra forma de sintaxis para usar el SLICING es:

print(text[:6]) #Se dice que se obvia el inicio que siempre es 0

print(text[5:]) #Se dice que se obvia el final entonces iria hasta el final de la cadena de texto


#Saltos, ademas de poder trabajar con las posiciones podemos usar un tercer parametro para indicar saltos entre las letras 

print(text[11:20:1]) #Saltaria de 1 en 1 
print(text[11:20:2]) #Slataria de 2 en 2 imprimiendo pormr