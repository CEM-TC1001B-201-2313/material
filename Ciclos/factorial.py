# factorial
# 5! = 5 * 4 * 3 * 2 * 1 = 120
# 5! = 1 * 2 * 3 * 4 * 5 = 120

# Genera un programa que pida como entrada un número entero y calcule
# y muestre su factorial.

numero = int(input("Ingresa el número al que calcularemos su factorial: "))

factorial = 1
for i in range(numero, 1, -1):
    #factorial = factorial * i
    factorial *= i
print(f"El factorial de {numero} es: {factorial}")
