udf1 = float(input("Ingresa tu calificación de tu udf1: "))
udf2 = float(input("Ingresa tu calificación de tu udf2: "))
udf3 = float(input("Ingresa tu calificación de tu udf3: "))
udf4 = float(input("Ingresa tu calificación de tu udf4: "))
udf5 = float(input("Ingresa tu calificación de tu udf5: "))
udf6 = float(input("Ingresa tu calificación de tu udf6: "))
udf7 = float(input("Ingresa tu calificación de tu udf7: "))

promedio = (udf1 + udf2 + udf3 + udf4 + udf5 + udf6 + udf7) / 7

print("El promedio fue:", promedio, "Sigue así.")
print("El promedio fue: " + str(promedio) + " Sigue así.")
print("El promedio fue: {0} Sigue así.".format(promedio))
print(f"El promedio fue: {promedio} Sigue así")

x = 4345665432.658832
# : -> formato especial
# , -> separador de miles
# .2 -> redondea a 2 decimales
# f -> formato tipo float en lugar de científico
print("x = {0:,.2f}".format(x))
print(f"x = {x:,.2f}")