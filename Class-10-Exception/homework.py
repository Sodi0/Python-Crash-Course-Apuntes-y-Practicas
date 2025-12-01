def par_impar(numero):
    if numero % 2 == 0:
        return "El número es par."
    else:
        return "El número es impar."

try:
    numero_input = int(input("Ingrese un número entero: "))
    resultado = par_impar(numero_input)
    print(resultado)
except ValueError:
    print("Error: Debe ingresar un número entero válido.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")


# Task 2
def dividir_numeros(num1, num2):
    return num1 / num2

try:
    numero_1, numero_2 = int(input("Ingrese el primer número entero: ")), int(input("Ingrese el segundo número entero: "))
    if numero_2 == 0:
        raise ZeroDivisionError("No se puede dividir por cero.")
    else:
        resultado_division = dividir_numeros(numero_1, numero_2)
        print(f"El resultado de la división es: {resultado_division}")
except ValueError:
    print("Error: Debe ingresar números enteros válidos.")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
finally:
    print("Gracias por usar el programa de división.")

# Task 3
def verificar_edad(edad):
    if edad % 2 == 0:
        return "La edad es par."
    else:
        return "La edad es impar."

try:
    edad_input = int(input("Ingrese su edad: "))
    if edad_input < 0:
        raise ValueError("La edad no puede ser negativa.")
    else:
        resultado_edad = verificar_edad(edad_input)
        print(f"{resultado_edad}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
finally:
    print("Gracias por usar el programa de verificación de edad.")