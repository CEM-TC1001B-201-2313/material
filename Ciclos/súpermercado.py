print("Bienvenido al súpermercado")

precio = 0
total = 0
while precio >= 0:
    total = total + precio
    precio = float(input("Introduce el precio del producto: "))
print(f"El total a pagar es: ${total:,.2f}")