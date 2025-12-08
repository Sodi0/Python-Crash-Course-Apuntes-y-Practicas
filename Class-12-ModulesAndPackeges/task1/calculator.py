from operations import suma, resta, multiplicacion, division

salir = False
while not salir:
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    eleccion = input("Ingrese su elección (1/2/3/4/5): ")

    if eleccion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if eleccion == '1':
            print(f"{num1} + {num2} = {suma(num1, num2)}")

        elif eleccion == '2':
            print(f"{num1} - {num2} = {resta(num1, num2)}")
        elif eleccion == '3':
            print(f"{num1} * {num2} = {multiplicacion(num1, num2)}")

        elif eleccion == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {division(num1, num2)}")
            else:
                print("Error: División por cero no permitida.")

    elif eleccion == '5':
        salir = True
        print("Saliendo del programa.")

    else:
        print("Entrada inválida. Por favor, intente de nuevo.")