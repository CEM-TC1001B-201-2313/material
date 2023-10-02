numero = int(input("Ingresa el número final de la sumatoria: "))

i = 1
sumatoria = 0
while i <= numero:
    sumatoria = sumatoria + i
    i += 1
print(f"El resultado de la sumatoria de 1 hasta {numero} es: {sumatoria}")