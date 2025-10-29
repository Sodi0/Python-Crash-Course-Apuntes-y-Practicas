# Convertir una lista de enteros en una lista de números decimales utilizando comprensión de listas.
my_list = [1, 2, 3, 4, 5, 8, 13, 21]

list_decimal = [float(item) for item in my_list]
print(list_decimal)