# Task 1: En el rango del 1 al 10, determine:
# los números pares que son divisibles por 2,
# los números impares que son divisibles por 3,
# los números que no son divisibles ni por 2 ni por 3.

listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

listaDivisiblesPorDos = []
listaDivisiblesPorTres = []
listaNoDivisiblesPorDosNiTres = []

for numero in listaNumeros:
    if numero % 2 == 0:
        listaDivisiblesPorDos.append(numero)
    if numero % 3 == 0:
        listaDivisiblesPorTres.append(numero)
    if numero % 2 != 0 and numero % 3 != 0:
        listaNoDivisiblesPorDosNiTres.append(numero)

print("Números divisibles por 2:", listaDivisiblesPorDos)
print("Números divisibles por 3:", listaDivisiblesPorTres)
print("Números no divisibles por 2 ni por 3:", listaNoDivisiblesPorDosNiTres)
print("\n")


# Task 2: 
# Escribe un script que verifique el nombre de usuario que introduce el usuario.
# Si el nombre de usuario es "Nombre", saluda al usuario. Si el nombre de usuario es diferente,
# muestra un mensaje de error.
# (Debes usar un bucle while)

print("---- TAREA 2 ----")
usuario = input("Ingrese su nombre: ").capitalize()
login = "First"

while login != usuario:
    print("Nombre de usuario incorrecto. Intente nuevamente.")
    usuario = input("Ingrese su nombre: ").capitalize()

print("¡Bienvenido,", usuario + "!")