# Apuntes: Módulos y Paquetes en Python

## Conceptos Fundamentales

**Diferencias clave:**
- **Módulo**: Un archivo `.py` con definiciones y declaraciones de Python
- **Paquete**: Namespace que contiene múltiples módulos/paquetes (directorio con `__init__.py`)
- **Biblioteca**: Colección de paquetes
- **Framework**: Colección de bibliotecas que arquitectura el flujo del código

## Módulos

### Características importantes:
- El nombre del módulo está disponible en `__name__`
- Tienen tablas de símbolos privadas
- Pueden ser **built-in** (integrados) o **definidos por el usuario**

### Formas de importar:

```python
# Importación básica
import module_name

# Importar objetos específicos
from module_name import function1, function2

# Importar todo (NO recomendado en producción)
from module_name import *

# Importar con alias
import module_name as alias
from module_name import function as f
```

### Puntos críticos:

1. **`__name__` y `__main__`**: 
   - Si ejecutas un archivo directamente: `__name__ == '__main__'`
   - Si lo importas como módulo: `__name__ == 'nombre_del_modulo'`

2. **Función `dir()`**: Retorna lista de nombres definidos en un namespace

3. **Ruta de búsqueda de módulos** (`sys.path`):
   - Directorio actual
   - Directorios en `PYTHONPATH`
   - Directorio de instalación por defecto

## Paquetes

### Estructura típica:
```
Customer/              # paquete principal
    __init__.py       # puede estar vacío (≥Python 3.3)
    Salary/           # subpaquete
        __init__.py
        info.py
    Personal/
        __init__.py
        position.py
```

### Formas de importar desde paquetes:

```python
# Nombre completo
import Customer.Personal.position
Customer.Personal.position.function()

# Importar submódulo
from Customer.Personal import position
position.function()

# Importar función directa
from Customer.Personal.position import function
function()
```

### Variable `__all__`:
En `__init__.py` puedes definir qué se importa con `from package import *`:
```python
__all__ = ["module1", "module2", "module3"]
```

## PIP - Gestor de Paquetes

### Comandos esenciales:

```bash
# Instalación
pip install SomePackage           # última versión
pip install SomePackage==1.0.4    # versión específica
pip install SomePackage>=1.3      # versión mínima
pip install SomePackage~=2.1      # compatible release

# Gestión
pip uninstall package_name
pip list                          # listar instalados
pip freeze > requirements.txt     # guardar dependencias
pip install -r requirements.txt   # instalar desde archivo
```

### Archivo `requirements.txt`:
```
# Sin versión específica
beautifulsoup4

# Con especificadores
docopt==0.6.1        # versión exacta
keyring>=4.1.1       # versión mínima
coverage!=3.5        # excluir versión
```

## Módulo RegEx (`re`)

### Funciones principales:

```python
import re

re.match(pattern, string)      # busca al inicio
re.search(pattern, string)     # busca en cualquier parte
re.findall(pattern, string)    # retorna lista con todas las coincidencias
re.split(pattern, string)      # divide string en cada coincidencia
re.sub(pattern, repl, string)  # reemplaza coincidencias
re.compile(pattern)            # compila patrón para reusar
```

### Metacaracteres importantes:
- `[]`: Conjunto de caracteres
- `\d`: Dígito [0-9]
- `\w`: Carácter alfanumérico
- `\s`: Espacio en blanco
- `^`: Inicio de string
- `$`: Final de string
- `*`: 0 o más repeticiones
- `+`: 1 o más repeticiones
- `{n,m}`: Entre n y m repeticiones

## Beneficios de usar Módulos

1. **Código estructurado**: Organización lógica y menos propenso a errores
2. **Reutilización**: Elimina código duplicado
3. **Mantenibilidad**: Más fácil de entender y usar
4. **Namespace**: Evita colisiones de nombres

## Recursos útiles mencionados

- PyPI: https://pypi.org/ (repositorio de paquetes)
- PyOWM: Biblioteca para OpenWeatherMap APIs
- RegEx testers: https://regex101.com/, https://pythex.org/

---

**Nota importante**: Desde Python 3.3+, `__init__.py` no es obligatorio, pero sigue siendo una buena práctica incluirlo para claridad.