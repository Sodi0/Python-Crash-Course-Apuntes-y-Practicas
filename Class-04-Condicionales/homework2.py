numero = int(input("Ingrese un número: "))

if numero == 0:
    print("El número es cero.")
elif numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")