numero = int(input("Ingresa el número para calcular su tabla de multiplicar:"))

i = 1
while i <= 10:
    resultado = i * numero
    print(f"{numero} x {i} = {resultado}")
    i += 1
