
# range(final) -> Genera una secuencia numérica que inicia en 0,
# avanza de 1 en 1 y termina antes de final
# range(5) -> 0,1,2,3,4
for i in range(5):
    print(f"El valor de i es: {i}")

print("-" * 30)
# range(inicio, final) -> Genera una secuencia numérica que inicia en
# inicio, avanza de 1 en 1 y termina antes de final
for i in range(5, 10):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

# range(inicio, final, paso) -> Genera una secuencia numérica que inica
# en inicio, avanza de paso en paso y termina antes de final
for i in range(5, 15, 3):
    print(f"El valor de i es: {i}")

print("-" * 30)

# Si la secuencia no puede ser generada, se obtiene una secuencia
# vacía y por lo tanto no se llevan a cabo repeticiones
for i in range(15, 5):
    print(f"El valor de i es: {i}")

print("-" * 30)

for i in range(1, 5, -1):
    print(f"El valor de i es: {i}")
    
print("-" * 30)

texto = "hola mundo"

for i in texto:
    print(f"El valor de i es: {i}")
    
print("-" * 30)

lista = [3, 6.3, "hola", [1,2], True]

for i in lista:
    print(f"El valor de i es: {i}")