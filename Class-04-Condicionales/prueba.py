# Validar si tres ángulos forman un triángulo válido
angulo_1 = 90
angulo_2 = 90
angulo_3 = 10

if (angulo_1 + angulo_2 + angulo_3 == 180) and (angulo_1 > 0) and (angulo_2 > 0) and (angulo_3 > 0):
    print("Es un triángulo válido")
else:
    print("NO es un triángulo válido")

# Validar si un número es par o impar
numero = 5
if numero % 2 == 0:
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")

# Encontrar el número mayor entre tres números
numero_1, numero_2, numero_3 = 9, 4 , 1
if numero_1 >= numero_2 and numero_1 >= numero_3:
    print(f"El número mayor es: {numero_1}")
elif numero_2 >= numero_1 and numero_2 >= numero_3:
    print(f"El número mayor es: {numero_2}")
else:
    print(f"El número mayor es: {numero_3}")

# Validar si un año es bisiesto
anio = 2020
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año ingresado es bisiesto")
else:
    print("El año ingresado NO es bisiesto")

# Validar si un caracter es vocal o consonante
caracter = 'B'
vocales = 'aeiou'

if caracter.lower() in vocales:
    print("El caracter ingresado es una vocal")
else:
    print("El caracter ingresado NO es una vocal")

# Asignar calificación basada en una nota numérica usando match-case
nota = 4.9

match nota:
    case n if n < 0 or n > 5:
        print("Nota inválida")
    case n if n >= 0 and n < 2:
        print("Nota deficiente")
    case n if n >= 2 and n < 3:
        print("Nota insuficiente")
    case n if n >= 3 and n < 4.5:
        print("Nota aceptable")
    case n if n >= 4.5 and n <= 5:
        print("Nota sobresaliente")