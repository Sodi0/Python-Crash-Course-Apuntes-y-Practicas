num1, num2 = 1, 1

def dividir(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        return "ERROR: Se realizó una división sobre cero"
    else:
        return f"{resultado}" + "\nLa división se realizó correctamente"
    
print(dividir(num1, num2))


# Question 2
proveedores = ['AWS','Azure','GCP','Alibaba Cloud','IBM']
mi_proveedor = 'AWS'

def buscar_proveedor(proveedor):
    try:
        if proveedor not in proveedores:
            raise NoTop5CloudProviderError
    except NoTop5CloudProviderError as e:
        return str(e)
    else:
        return f"{proveedor}"

class NoTop5CloudProviderError(Exception):
    def __init__(self, data="ADVERTENCIA: No es un proveedor cloud en el Top 5."):
        self.data = data
    def __str__(self):
        return self.data
    
print(buscar_proveedor(mi_proveedor))

# Question 3
mi_lista = ['Lviv','Kiev','Varsovia','Medellín','Santiago']
indice = "13"

def buscar_ciudad(lista, indice):
    try:
        ciudad = lista[int(indice)]
    except IndexError:
        return "ERROR: Debe ingresar un índice existente"
    except ValueError:
        return "ERROR: Debe ingresar un número válido"
    else:
        return f"{ciudad}"

print(buscar_ciudad(mi_lista, indice))