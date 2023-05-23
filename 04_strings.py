my_name = "Paco"
last_name = "Lopez"
my_age = 39

# Concatenacion de Strings

full_name = my_name + " " + last_name
print(full_name)
type(full_name)

quote = "I´m Paquito"
print(quote)


quote2 = 'She said "Hello"'
print(quote2)


# Strings Format

template = "Hola, mi nombre es " + my_name + " y mi apellido es " + last_name
print(template)

template2 = "Hola, mi nombre es {} y mi apellido es {}".format(my_name, last_name)
print(template2)

template3 = f"Hola, mi nombre es {my_name} y mi apellido es {last_name}, mi edad es de {my_age} años"

print(template3)
