# Tabla de mulitiplicar
# Introducir un número y vamos a mostrar su tabla de multiplicar del 1 al 10
# Si numero = 3
# 1 x 3 = 3
# 2 x 3 = 6
# ...
# 10 x 3 = 30

numero = int(input("Ingrese su número: "))
for i in range(1,11):
    res = numero * i
    print(f"{i} x {numero} = {res}")