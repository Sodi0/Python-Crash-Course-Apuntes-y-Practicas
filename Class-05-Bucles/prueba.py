numero_1 = 1
numero_2 = 1
total = 0
while numero_1 <= numero_2:
    if numero_1 % 2 != 0:
        total += numero_1
    numero_1 += 1

print(total)

numero = 3
for i in range(numero + 1):
    print(i)

numero = 4

if numero < 2:
    print(f'{numero} NO es un número primo')
elif all(numero % i != 0 for i in range(2, numero)):
    print(f'{numero} es un número primo')
else:
    print(f'{numero} NO es un número primo')

numero = 3
# n - 1 hasta el 0 
for i in range(numero, -1, -1):
    print(i)


#piramide sin espacios
altura = int(input("Introduce la altura de la pirámide: "))
for i in range(1, altura + 1):
    print('*' * i)

# numeros impares hasta n
n = int(input("Introduce un número entero positivo: "))
for i in range(n + 1):
    if i % 2 != 0:
        print(i)

# factorial de un número
n = int(input("Introduce un número entero positivo para calcular su factorial: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(factorial)