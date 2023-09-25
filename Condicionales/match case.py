
menu = int(input("""Menú:
1) Consultar saldo.
2) Depositar dinero.
3) Retirar dinero.
0) Cancelar
Ingresa la opción deseada: """))

match menu:
    case 1:
        print("Tu saldo es...")
    case 2:
        print("Depositando dinero...")
    case 3:
        print("Retirando dinero...")
    case 0:
        print("Hasta luego.")
    case _: # Caso por default
        print("Opción no válida.")