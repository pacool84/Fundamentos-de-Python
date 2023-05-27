name = "Paco"
print(type(name))

name = 12
print(type(name))

name = True
print(type(name))


print("Paco " + "Lopez")
print(10 + 20)

# No es posible concatenar tipos de datos strings con numeros

print("Hola, mi edad es " + 12)

# Tranformando a tipo de dato string utilizando el operador STR
age = 12
new_age = str(age)
print(type(new_age))

print("Hola, mi edad es " + new_age)


# utilizando la funcion format f podemos concatenar strings y numeros

age = 39
print(type(age))
print(f"Hola, mi edad es de {age}")

# Siempre que utilicemos input nos regresara un string

# Tranformando a tipo de dato number utilizando el operador INT

age = input("Cual es tu edad? ")
print(type(age))

age_tranformed = int(age)
age_tranformed += 10
print(f"Tu edad en 10 años sera {age_tranformed}")
print("Tu edad en 10 años sera", age_tranformed)


# En este desafío, se te proporcionará un código base encontrarás las variables name y age todas como strings. Tu tarea es crear un formato de string que, como resultado, muestre un mensaje en la sección Terminal. El mensaje deberá tener la siguiente forma:
# Hola mi nombre es {name}, tengo {age} años y en 10 años tendré {total} años

name = "Paco"
print(name)
age = "39"
print(age)

age = int(age)
print(type(age))
future_age = age + 10

template = (
    f"Hola mi nombre es {name}, tengo {age} años y en 10 años tendre {future_age} años "
)
print(template)
