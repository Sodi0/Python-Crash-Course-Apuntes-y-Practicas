# Ejercicio 2: Imprimir los primeros n números de Fibonacci
numero = int(input("Introduce cuántos números de Fibonacci quieres mostrar: "))

# while
a, b = 0, 1
count = 0
while count < numero:
    print(a)
    a, b = b, a + b
    count += 1
