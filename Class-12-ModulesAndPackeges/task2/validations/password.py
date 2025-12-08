def validar_contrasenia(contrasenia):
    errores = []
    if not validar_longitud(contrasenia):
        errores.append("La longitud debe ser entre 6 y 16 caracteres.")
    if not validar_letras(contrasenia):
        errores.append("Debe contener al menos una letra minúscula y una letra mayúscula.")
    if not validar_numero(contrasenia):
        errores.append("Debe contener al menos un número.")
    if not validar_caracter_especial(contrasenia):
        errores.append("Debe contener al menos un carácter especial entre [$#@].")
    if not validar_longitud(contrasenia):
        errores.append("La longitud debe ser entre 6 y 16 caracteres.")
    
    return errores

def validar_longitud(contrasenia):
    return 6 <= len(contrasenia) <= 16

def validar_caracter_especial(contrasenia):
    caracteres_especiales = set("$#@")
    return any(char in caracteres_especiales for char in contrasenia)

def validar_numero(contrasenia):
    return any(char.isdigit() for char in contrasenia)

def validar_letras(contrasenia):
    tiene_minuscula = any(char.islower() for char in contrasenia)
    tiene_mayuscula = any(char.isupper() for char in contrasenia)
    return tiene_minuscula and tiene_mayuscula