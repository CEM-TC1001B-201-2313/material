
alumnos = ["Sofía", "Jade", "Daniel", "Hannia", "Yaz"]

nombre = input("Introduce el nombre a buscar: ")
encontrado = False
for i in alumnos:
    if nombre == i:
        encontrado = True
# encontrado == True
# True == True -> True
# False == True -> False
if encontrado:    
    print("Alumno encontrado.")
else:
    print("Alumno no encontrado.")
    
# --------------------------------

for i in alumnos:
    if nombre == i:
        print("Alumno encontrado.")
        break # finaliza el ciclo - ya no ejecuta el resto de las iteraciones
else: # ejecuta sus líneas de codigo si el ciclo terminó su recorrido, no pasó por break
    print("Alumno no encontrado.")
