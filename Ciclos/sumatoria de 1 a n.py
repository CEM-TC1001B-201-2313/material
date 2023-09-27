# Crear un programa que me calcule la suma de todos los números
# desde 1 hasta un número que el usuario indique

numero = int(input("Indique el número hasta el que quiere llegar: "))
suma = 0
for i in range(1, numero + 1):
    #suma = suma + i
    suma += i
print(f"La suma de números de 1 a {numero} es: {suma}")