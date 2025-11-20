# Question 1
def numeros_primos(numero_1, numero_2):
    primos = []
    for num in range(numero_1, numero_2 + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primos.append(num)
    return primos

print(numeros_primos(1, 10))

#Question 2
def mayor_menor(lista):
    mayor = max(lista)
    menor = min(lista)
    numeros = tuple((mayor, menor))
    return numeros

print(mayor_menor([8.7, 9.3, 87.0, 45, 123, 78.23, 0, -4.5]))

# Question 3
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

# Question 4
def area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

print(area_triangulo(0,0))

# Question 5
def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        numero = numero * factorial(numero - 1)
    return numero

print(factorial(4))

# Question 6
def es_impar(numero):
    return numero % 2 != 0

print(es_impar(0))