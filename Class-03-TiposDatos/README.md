# Built-in Types en Python

## 📌 Conceptos Fundamentales

### Características de Python
- **Lenguaje dinámicamente tipado**: no necesitas declarar el tipo de variable
- **Case-sensitive**: `Variable` ≠ `variable`
- **Variables son referencias**: apuntan a objetos en memoria, no contienen valores directamente

### Convenciones de Nombres
```python
# ✅ Válidos
myClass
var_1
print_this_to_screen

# Estilos comunes
snake_case    # Python estándar
camelCase     # Menos común en Python
kebab-case    # NO válido en Python (no usar -)
```

---

## 🔄 Mutabilidad vs Inmutabilidad

### Tipos Inmutables (no se pueden modificar)
- `bool`, `int`, `float`, `str`, `tuple`, `frozenset`

### Tipos Mutables (se pueden modificar)
- `list`, `set`, `dict`

### Ejemplo de la diferencia:
```python
# INMUTABLE (string)
x = 'foo'
y = x
y += 'bar'
print(x)  # 'foo' - no cambia

# MUTABLE (list)
x = [1, 2, 3]
y = x
y += [3, 2, 1]
print(x)  # [1, 2, 3, 3, 2, 1] - sí cambia!
```

### Truco: Usar `id()` para verificar mutabilidad
```python
# Inmutable: el id CAMBIA
i = 1
id(i)  # 704
i += 1
id(i)  # 736 (diferente)

# Mutable: el id NO CAMBIA
a = [1]
id(a)  # 416
a.append(2)
id(a)  # 416 (mismo)
```

---

## 📦 Tipos de Datos Principales

### 1. Numéricos
```python
int_num = 12
float_num = 12.5
complex_num = 3 + 4j
bool_val = True  # True/False
```

### 2. Secuencias
```python
# Lista (mutable)
my_list = ['abcd', 786, 2.23, 'john', 70.2]

# Tupla (inmutable)
my_tuple = ('abcd', 786, 2.23, 'john', 70.2)

# String (inmutable)
my_str = "My name is..."
```

### 3. Conjuntos
```python
# Set (mutable, sin duplicados)
my_set = set('qwerty')  # {'e', 'q', 'r', 't', 'w', 'y'}

# Frozenset (inmutable)
my_frozenset = frozenset('qwerty')
```

### 4. Diccionarios
```python
# Dict (mutable, pares clave-valor)
my_dict = {'name': 'john', 'id': 6734, 'role': 'admin'}
```

---

## 🔍 Verificar Tipos

```python
# Obtener el tipo
type([])     # <class 'list'>
type({})     # <class 'dict'>
type('')     # <class 'str'>

# Verificar tipo específico
type([]) is list    # True
isinstance([], list)  # True
```

---

## 🔄 Conversión de Tipos

### Conversión Implícita (automática)
```python
num_int = 123
num_float = 1.23
result = num_int + num_float  # 124.23 (convierte a float)
```

### Conversión Explícita (manual)
```python
# A entero
int("34")        # 34
int("0100", 2)   # 4 (binario)
int(6.7)         # 6 (trunca)
int("0xfe", 16)  # 254 (hexadecimal)

# A float
float("3")       # 3.0

# A string
str(10)          # "10"

# Entre colecciones
tuple([1, 2, 3])  # (1, 2, 3)
list((1, 2, 3))   # [1, 2, 3]
set([1, 1, 2])    # {1, 2}

# Evaluar expresiones
eval("3 + 5")     # 8
```

---

## 📝 Strings

### Crear strings
```python
my_string = 'Hello'
my_string = "Hello"
my_string = '''Multi
line
string'''
```

### Indexing y Slicing
```python
str = 'programiz'
str[0]      # 'p' (primer carácter)
str[-1]     # 'z' (último carácter)
str[1:5]    # 'rogr' (del índice 1 al 4)
str[5:-2]   # 'am' (del 5 al penúltimo-1)
```

### Métodos comunes
```python
"PrOgRaMiZ".lower()                    # 'programiz'
"programiz".upper()                    # 'PROGRAMIZ'
"word1 word2".split()                  # ['word1', 'word2']
' '.join(['a', 'b'])                   # 'a b'
'Happy New Year'.find('ew')            # 7
'Happy New Year'.replace('Happy', 'Good')  # 'Good New Year'
```

### Formateo de Strings

#### 1. Operador % (antiguo)
```python
name = "John"
age = 23
print("%s is %d years old" % (name, age))
# John is 23 years old
```

#### 2. Método .format()
```python
"{}, {} and {}".format('John', 'Bill', 'Sean')
# 'John, Bill and Sean'

"{0:.3f}".format(1/3)  # '0.333' (3 decimales)
```

#### 3. f-strings (Python 3.6+, RECOMENDADO)
```python
name = "Liubov"
age = 20
message = f"Hi {name}. You are {age} years old."
# Hi Liubov. You are 20 years old.
```

### Caracteres de Escape
```python
\n   # Nueva línea
\r   # Inicio de línea
\t   # Tabulación
\'   # Apóstrofe
\"   # Comillas
\\   # Barra invertida

# Raw strings (ignora escapes)
print(r"Hello \n world")  # Hello \n world
```

---

## ➕ Operadores Aritméticos

| Operador | Nombre | Ejemplo | Resultado |
|----------|---------|---------|-----------|
| `+` | Suma | `7 + 3` | `10` |
| `-` | Resta | `7 - 3` | `4` |
| `*` | Multiplicación | `7 * 3` | `21` |
| `/` | División | `7 / 3` | `2.333...` |
| `//` | División entera | `7 // 3` | `2` |
| `%` | Módulo (resto) | `7 % 3` | `1` |
| `**` | Exponente | `3 ** 2` | `9` |

### Operadores de Asignación Compuesta
```python
i += 5   # i = i + 5
i -= 5   # i = i - 5
i *= 5   # i = i * 5
i /= 5   # i = i / 5
i //= 5  # i = i // 5
i %= 5   # i = i % 5
i **= 5  # i = i ** 5
```

---

## 📋 Variables y Constantes

### Declarar variables
```python
# Asignación simple
variable = 10

# Múltiples variables
a, b, c = 1, 2, 3

# Mismo valor a múltiples variables
x = y = z = 100
```

### Constantes (por convención)
```python
PI = 3.14159
MAX_SIZE = 1000
DATABASE_URL = "localhost:5432"
```

---

## 📄 Sintaxis Básica

### Statements y Continuación de Línea
```python
# Múltiples líneas con \
total = 1 + 2 + 3 + \
        4 + 5 + 6

# Continuación implícita con (), [], {}
my_list = [
    1, 2, 3,
    4, 5, 6
]

# Múltiples statements en una línea (evitar)
a = 1; b = 2; c = 3
```

### Indentación (¡IMPORTANTE!)
```python
# ✅ Correcto (4 espacios)
if True:
    print("Hello")
    print("World")

# ❌ Incorrecto (inconsistente)
if True:
    print("Hello")
  print("World")  # IndentationError
```

---

## 📚 Literales

### Literales Numéricos
```python
binary = 0b1010      # Binario
octal = 0o12         # Octal
hexadecimal = 0xFF   # Hexadecimal
```

### Literal Especial: None
```python
value = None  # Representa ausencia de valor
```

### Literales de Colección
```python
list_literal = [1, 2, 3]
tuple_literal = (1, 2, 3)
set_literal = {1, 2, 3}
dict_literal = {'key': 'value'}
```

---

## ✅ TAREAS

### Tarea 1: Filosofía de Python
Dado el siguiente string con la filosofía de Python:
```python
text = "Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex."
```

**Hacer:**
1. Encontrar el número de veces que aparecen las palabras: "better", "never" e "is"
2. Mostrar todo el texto en MAYÚSCULAS
3. Reemplazar todas las ocurrencias de la letra "i" con "&"

### Tarea 2: Número de 4 dígitos
Dado un número natural de 4 dígitos (ejemplo: 1234):

**Hacer:**
1. Encontrar el producto de todos los dígitos
2. Escribir el número en orden inverso
3. Ordenar los dígitos en orden ascendente

### Tarea 3: Intercambio de Variables
Intercambiar los valores de dos variables **sin usar una tercera variable**.

**Ejemplo:**
```python
a = 5
b = 10
# Después del intercambio: a = 10, b = 5
```

---

## 💡 Tips Importantes

1. **Siempre usa f-strings** para formateo (Python 3.6+)
2. **Cuidado con mutabilidad**: `b = a` con listas hace que ambas apunten al mismo objeto
3. **Usa `is` para comparar con None**: `if value is None:`
4. **4 espacios para indentación** (no tabs)
5. **Constantes en MAYÚSCULAS** por convención
6. **Snake_case** para variables y funciones en Python

---

## 📖 Recursos Adicionales

- [Métodos de String](https://www.programiz.com/python-programming/methods/string)
- Usa `dir(objeto)` para ver todos los métodos disponibles

```python
dir("")  # Ver todos los métodos de string
help(str.replace)  # Ver documentación de un método
```