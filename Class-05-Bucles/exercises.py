# Ejercicio 1: Imprimir números pares del 0 al 100

# while
start = 0
finish = 100

while start <= finish:
    print(start)
    start += 2

# for
for number in range(0, 101, 2):
    print(number)

# Ejercicio 2: Imprimir números impares del 0 al 100
start = 1
while start <= finish:
    print(start)
    start += 2

for number in range(1, 101, 2):
    print(number)
