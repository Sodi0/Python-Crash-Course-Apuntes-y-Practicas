# Python - Fundamentos y Sintaxis

## ¿Qué es Python?

- Lenguaje interpretado, interactivo y orientado a objetos
- Alto nivel, de propósito general
- Énfasis en legibilidad del código
- Tipado dinámico y gestión automática de memoria
- Usa indentación en lugar de llaves para delimitar bloques

## Comentarios

```python
# Comentario de una línea

# Comentario
# multi-línea
# con varios #

"""
Comentario multi-línea
usando triple comillas
"""
```

## Variables

- No necesitan declaración de tipo
- Se crean al asignarles un valor (inicialización)
- Sensibles a mayúsculas/minúsculas: `val` ≠ `Val`
- Python asigna referencias a objetos, no valores directos

```python
count = 10
variable1 = "texto"
```

## Identificadores

**Reglas:**
- Combinación de letras (a-z, A-Z), dígitos (0-9) y guión bajo (_)
- No pueden empezar con dígito
- No usar palabras reservadas (keywords)
- No usar símbolos especiales (!, @, #, $, %)
- Cualquier longitud

**Convenciones:**
- `snake_case`: `this_is_a_variable`
- `camelCase`: `camelCaseExample`

## Palabras Reservadas (Keywords)

35 palabras reservadas en Python (case-sensitive):
```python
import keyword
print(keyword.kwlist)
```

## Operadores

### Operadores Aritméticos
- `+` suma
- `-` resta
- `*` multiplicación
- `/` división
- `%` módulo
- `//` división entera
- `**` potencia

```python
number = 3 + 4 * 5 ** 2 + 7
number = (3 + 4) * (5 ** 2 + 7)
number = 2**3**2  # Potencia asocia de derecha a izquierda
```

### Operadores Lógicos
- `and` (&&)
- `or` (||)
- `not` (!)

### Operadores de Comparación
- `==` igualdad
- `=` asignación

### Operadores Especiales
- `+` concatenación de strings
- `%` formateo de strings

## Indentación

- Python usa espacios para delimitar bloques
- Incremento de indentación después de ciertas declaraciones
- Decremento marca el fin del bloque actual
- Usar `\` para continuar en la siguiente línea

```python
if condition:
    # bloque indentado
    statement1
    statement2
# fin del bloque
```

## Entrada/Salida

```python
# Salida
print("Hola mundo")

# Entrada
nombre = input("Ingresa tu nombre: ")
```

## PEP 8 - Guía de Estilo

### Indentación
- Usar 4 espacios por nivel
- Alinear con el delimitador de apertura

### Longitud de Línea
- Máximo 79 caracteres para código
- Máximo 72 caracteres para comentarios/docstrings

### Líneas en Blanco
- 2 líneas en blanco antes y después de definiciones de clase
- 1 línea en blanco antes y después de definiciones de método
- Usar con moderación dentro del código

### Codificación
- UTF-8 por defecto
- Identificadores solo ASCII en la biblioteca estándar

### Imports
- En líneas separadas
- Al inicio del archivo (después de comentarios y docstrings)

```python
import os
import sys

from subprocess import Popen, PIPE
```

## Zen de Python

```python
import this
```

Principios clave:
- Bello es mejor que feo
- Explícito es mejor que implícito
- Simple es mejor que complejo
- La legibilidad cuenta
- Debe haber una forma obvia de hacerlo

## Recursos

- Documentación oficial: [python.org](https://python.org/)
- Tutorial interactivo: [python.swaroopch.com](https://python.swaroopch.com/)
- Guía de estilo: [PEP 8](https://peps.python.org/pep-0008/)