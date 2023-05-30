x = 3.3
y = 1.1 + 2.2

print(x)
print(y)  # Tiene una precision decimal mayor

print(x == y)  # Esto es falso por la presicion decimal

# Existen dos formas para comparar los flotantes

# La primera es tranformarlos a Strings

y_str = format(y, ".2g")
print(y_str)
print(type(y_str))

x_str = str(x)
print(type(x_str))


print(x_str == y_str)

# La Segunda forma es utilizando matematicas, utilizando tolerancia

TOLERANCE = 0.00001
print(
    abs(x - y) < TOLERANCE
)  # La funcion abs es para obtener el valor absoluto y no trabajar con numeros negativos
