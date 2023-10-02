
# for i in range(1,10,3)
i = 1 # Valor inicial de la variable de control
while i <= 10: # Condición de paro o de salida
    print(f"El valor de i es: {i}")
    #i = i + 3
    i += 3 # Paso
    
print("-"*30)

texto = "Hola mundo"
# for i in texto:
i = 0
while i < len(texto):
    print(f"texto[{i}] = {texto[i]}")
    i += 1

print("-"*30)

lista = [1,2,"hola",True]
# for i in lista:
i = 0
while i < len(lista):
    print(f"lista[{i}] = {lista[i]}")
    i += 1
    
print("-"*30)

salir = "n"
while salir != "s":
    print("Ejecutando resto del programa...")
    salir = input("¿Desea salir del programa? s/n: ").strip().lower()