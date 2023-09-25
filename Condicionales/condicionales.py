
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad. Ya puedes votar.")
else:
    restan = 18 - edad
    print(f"Te faltan {restan} años para poder votar.")