from validations import validar_contrasenia

print("Verificador de contraseñas")
print("La contraseña debe cumplir con los siguientes requisitos:")
print("""
- Al menos una letra entre [a-z] y una letra entre [A-Z].
- Al menos un número entre [0-9].
- Al menos un carácter entre [$#@].
- Longitud mínima: 6 caracteres.
- Longitud máxima: 16 caracteres.
""")
contrasenia = input("Introduce una contraseña: ")

errores = validar_contrasenia(contrasenia)

if errores:
    for error in errores:
        print("X", error)
else:
    print("✔ Contraseña válida")
