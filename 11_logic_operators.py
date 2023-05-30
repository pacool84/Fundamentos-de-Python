# Operador AND
print("Operador AND")

print("True and True => ", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

# Otras formas de utilizar el operador AND

print(5 < 10 and 10 > 5)
print(10 > 5 and 5 > 10)

# Otro ejemplo practico
# Evaluando un maximo y minimo de cantidades

STOCK = input("Ingrese el número de stock ==> ")
STOCK = int(STOCK)
print(STOCK >= 100 and STOCK <= 1000)

# Operador OR,cualquier valor en True siempre dara True
print("Operador OR")

print("True or True =>", True or True)
print("True or False =>", True or False)
print("False or True =>", False or True)
print("False or False =>", False or False)

# Ejercicio practico, evaluando un rol

USER_ROLE = input("Digite el Rol =>")
print(USER_ROLE == "admin" or USER_ROLE == "developer")
