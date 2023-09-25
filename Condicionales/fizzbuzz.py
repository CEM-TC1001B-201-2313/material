# fizzbuzz
# ingresamos un número entero
# si el número es divisible entre 3 -> Fizz
# si el número es divisible entre 5 -> Buzz
# si el número es divisible entre 3 y 5 -> FizzBuzz
# si el número no es divisible ni entre 3 ni 5 -> número

numero = int(input("Ingresa el número a revisar: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
elif numero % 3 == 0:
    print("Fizz")
elif numero % 5 == 0:
    print("Buzz")
else:
    print(numero)