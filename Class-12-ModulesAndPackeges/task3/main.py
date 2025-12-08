from calculation_area import area_circulo, area_triangulo, area_rectangulo

salir = False

while not salir:
    print("Seleccione una opción:")
    print("1. Calcular área del círculo")
    print("2. Calcular área del triángulo")
    print("3. Calcular área del rectángulo")
    print("4. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == '1':
        radio = float(input("Ingrese el radio del círculo: "))
        area = area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")
    elif opcion == '2':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")
    elif opcion == '3':
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        area = area_rectangulo(largo, ancho)
        print(f"El área del rectángulo es: {area:.2f}")
    elif opcion == '4':
        salir = True
        print("Saliendo del programa.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")