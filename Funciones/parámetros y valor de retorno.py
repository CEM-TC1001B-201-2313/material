# parámetros -> entradas o datos que requiere la función
# valor de retorno -> salidas o el resultado de la función

# sin parámetros y sin valor de retorno
def suma1():
    x = float(input("Ingresa el valor de x: "))
    y = float(input("Ingresa el valor de y: "))
    resultado = x + y
    print(f"La suma de {x:,.2f} + {y:,.2f} = {resultado:,.2f}")

#suma1()
# con parámetros y sin valor de retorno
def suma2(x : float, y : float):
    resultado = x + y
    print(f"La suma de {x:,.2f} + {y:,.2f} = {resultado:,.2f}")

#suma2(14, 8)
#a = float(input("Proporciona el valor de x: "))
#b = float(input("Proporciona el valor de y: "))
#suma2(a, b)
    
# con parámetros y con valor de retorno
def suma3(x : float, y : float) -> float:
    resultado = x + y
    return resultado

res = suma3(2,3)
print(res)

res = suma3("hola", "mundo")
print(res)

res = suma2(2,3)
print(res)