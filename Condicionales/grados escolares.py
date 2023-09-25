
edad = int(input("Ingresa la edad del estudiante: "))

if edad < 3:
    print("No aplica.")
elif edad <= 5:
    print("Kinder.")
elif edad <= 11:
    print("Primaria.")
elif edad <= 14:
    print("Secundaria.")
elif edad <= 17:
    print("Preparatoria.")
else:
    print("Profesional.")
                    
if edad < 3:
    print("No aplica.")
else:
    if edad <= 5:
        print("Kinder.")
    else:
        if edad <= 11:
            print("Primaria.")
        else:
            if edad <= 14:
                print("Secundaria.")
            else:
                if edad <= 17:
                    print("Preparatoria.")
                else:
                    print("Profesional.")