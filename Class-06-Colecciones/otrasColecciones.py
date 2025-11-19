# ejercicio 1
diccionario = {'Suiza': 7.26, 'Uruguay': 6.85, 'Noruega': 6.59, 'Suecia': 5.62, 'Dinamarca': 5.41, 'Argentina': 5.31, 'Zona euro': 5.29, 'Estados Unidos': 5.15}
lista = ['Argentina', 'Uruguay']

nuevo_diccionario = {pais: diccionario[pais] for pais in lista if pais in diccionario}

print(nuevo_diccionario)

#ejercicio 2
tupla = ('Alemania', 'Alemania', 'Alemania')
if len(set(tupla)) == 1:
    print("True")
else:
    print("False")

#ejercicio 3
tupla_1 = ('C', 'Javascript')
tupla_2 = ('Rust', 'Python')

# Se invierten las tuplas con slicing [::-1]
tupla_1, tupla_2 = tupla_2[::-1], tupla_1[::-1]

print(tupla_1)
print(tupla_2)

#ejercicio 4
conjunto_1 = {2}
conjunto_2 = {1}
# Se calcula la intersección entre ambos conjuntos
conjunto_3 = conjunto_1 & conjunto_2
print(conjunto_3)

#ejercicio 5
lista_1 = [1, 2, 3]
lista_2 = ['Chile', 'Peru']

mi_diccionario = dict(zip(lista_1, lista_2))
print(mi_diccionario)