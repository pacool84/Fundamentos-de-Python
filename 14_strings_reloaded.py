text = "Sebas sabe programar en Python"

print(
    "JavaScript" in text
)  # El metodo in busca la palabra definida, considerar que es case sensitive

print("Python" in text)

if "Python" in text:
    print("Sebas si sabe Python")
else:
    print("Paco si sabe JavaScript")

# El metodo len cuenta la cantidad de letras y espacios en una cadena de texto
size = len(text)
print(size)


print(text.upper())  # El metodo upper transforma una cadena de texto en mayusculas

print(text.lower())  # El metodo lower transforma una cadena de texto a minisculas


# El metodo count cuenta la cantidad de letras o palabras en una cadena de texto
print(text.count("a"))
print(text.count("Python"))

# El metodo swapcase transforma las minusculas en mayusculas y viceversa

print(text.swapcase())

# El metodo startswith revisa si un texto inicia con algo en especifico, regresa un booleano

print(text.startswith("Sebas sabe"))


# El metodo endswith revisa si un texto termina con algo especifico

print(text.endswith("Python"))

# El metodo replace remplaza una cadena de texto por otra

print(text.replace("Python", "Servicenow"))


second_text = "este es un titulo"

print(second_text)

# El metodo capitalize coloca la primer letra del texto en mayusculas
print(second_text.capitalize())

# El metodo title cambia a mayuscula la primer letra de cada palabra
print(second_text.title())

#La funcion isdigit evalua si una cadena de texto podria ser un numero, regresa un boolenao

print(second_text.isdigit())
print("13".isdigit())