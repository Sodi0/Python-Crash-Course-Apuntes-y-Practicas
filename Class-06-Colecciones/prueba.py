# ---------- Pregunta 1 ----------
# Objetivo: eliminar elementos "vacíos" de una lista (en este caso, cadenas vacías).
# Entrada: `lista` contiene varios elementos, algunos son cadenas vacías ''.
# Salida: `nueva_lista` es una nueva lista que contiene solo los elementos truthy
# (las cadenas no vacías). Nota: la expresión `if elemento` filtra cualquier
# valor falsy de Python ('' (cadena vacía), 0, None, False, etc.).
lista = ['HTML', '1', 'jQuery', 'Angular', '', 'Angular', '', 'Ruby', 'C#', 'Python', '']

nueva_lista = [elemento for elemento in lista if elemento]
# Ejemplo: nueva_lista -> ['HTML', '1', 'jQuery', 'Angular', 'Angular', 'Ruby', 'C#', 'Python']


# ---------- Pregunta 2 ----------
# Objetivo: reemplazar todas las ocurrencias de un valor por otro en la lista.
# Entrada: `valor_anterior` (cadena a buscar) y `valor_nuevo` (cadena que sustituye).
# Salida: reasignación de `lista` a una nueva lista donde cada elemento igual a
# `valor_anterior` se reemplaza por `valor_nuevo`. La comparación es exacta y
# sensible a mayúsculas/minúsculas.
valor_anterior = "HTML"
valor_nuevo = "HTML5"

lista = [valor_nuevo if elemento == valor_anterior else elemento for elemento in lista]
# Ejemplo: cualquier 'HTML' en la lista se convertirá en 'HTML5'


# ---------- Pregunta 3 ----------
# Objetivo: imprimir los números negativos de una lista.
# Entrada: `lista` de enteros (puede incluir positivos, negativos y 0).
# Salida: impresión por pantalla de cada número negativo encontrado (uno por línea).
# Observaciones: el código usa indexing por posición (range(len(...))). Se puede
# escribir de forma más legible con `for x in lista:`.
lista = [0, 1, -2, 3, -4, 5, -6]
for i in range(len(lista)):
    if lista[i] < 0:
        # Aquí se imprime cada valor negativo. Ejemplo de salida: -2 \n -4 \n -6
        print(lista[i])


# ---------- Pregunta 4 ----------
# Objetivo: separar una lista en impares y pares, luego sumar los impares y
# multiplicar los pares.
# Entrada: `lista` de enteros.
# Salida: imprime primero la suma de los impares y luego la multiplicación de los pares.
# Casos y supuestos importantes:
# - Si no hay impares, `suma_impares` permanecerá en 0 (resultado razonable para una suma vacía).
# - Si no hay pares, `multiplicacion_pares` quedará como 1 (valor neutro de la multiplicación),
#   lo que puede ser confuso: en algunos contextos preferirías `None` o 0. Si la lista de pares
#   contiene el 0, el producto será 0.
# - El código actual usa `lista = [0]` como ejemplo; reemplazar por la lista real al usar.
lista = [0]
lista_impares = []
lista_pares = []
for i in range(len(lista)):
    if lista[i] % 2 != 0:
        lista_impares.append(lista[i])
    if lista[i] % 2 == 0:
        lista_pares.append(lista[i])

# Sumar impares (si no hay, el resultado será 0)
suma_impares = 0
for i in range(len(lista_impares)):
    suma_impares += lista_impares[i]

# Multiplicar pares (si no hay pares, el resultado quedará como 1)
multiplicacion_pares = 1
for i in range(len(lista_pares)):
    multiplicacion_pares *= lista_pares[i]

print(suma_impares)
print(multiplicacion_pares)