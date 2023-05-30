# Operator NOT

print(not True)
print(not False)

print("not True and True => ", not (True and True))
print("not True and False =>", not (True and False))
print("not False and True =>", not (False and True))
print("not False and False =>", not (False and False))


STOCK = input("Ingrese el número de stock ==> ")
STOCK = int(STOCK)
print(not (STOCK >= 100 and STOCK <= 1000))
