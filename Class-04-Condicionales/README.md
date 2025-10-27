# if Statements en Python

## 📋 Agenda
- Condiciones
- Declaraciones if
- Palabras clave: not, and, or
- Match Case (Python 3.10+)

---

## 🔀 Toma de Decisiones en Python

La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple cierta condición.

### Reglas de Evaluación
- Python interpreta valores **no-cero como True**
- **None** y **0** se interpretan como **False**

```python
if 5:           # True
    print("Non-zero is True")

if 0:           # False
    print("This won't print")

if None:        # False
    print("This won't print either")
```

---

## 🔍 Operadores de Comparación

Comparan valores y retornan `True` o `False`.

| Operador | Significado | Ejemplo (a=5, b=10) | Resultado |
|----------|-------------|---------------------|-----------|
| `==` | Igual a | `a == b` | `False` |
| `!=` | Diferente de | `a != b` | `True` |
| `>` | Mayor que | `a > b` | `False` |
| `<` | Menor que | `a < b` | `True` |
| `>=` | Mayor o igual que | `a >= b` | `False` |
| `<=` | Menor o igual que | `a <= b` | `True` |

### Ejemplos
```python
a = 5
b = 10

print(a == b)   # False
print(a != b)   # True
print(a < b)    # True
print(a >= b)   # False
```

---

## 🔗 Operadores Lógicos

En Python son **palabras** (and, or, not), no símbolos (&&, ||, !).

### Tabla de Verdad - AND
| A | B | A and B |
|---|---|---------|
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

### Tabla de Verdad - OR
| A | B | A or B |
|---|---|--------|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

### Tabla de Verdad - NOT
| A | not A |
|---|-------|
| 0 | 1 |
| 1 | 0 |

### Resumen de Operadores

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `and` | True si ambos operandos son True | `x and y` |
| `or` | True si al menos uno es True | `x or y` |
| `not` | Niega el operando (complemento) | `not x` |

### Ejemplos
```python
x = True
y = False

print(x and y)   # False
print(x or y)    # True
print(not x)     # False
print(not y)     # True

# Combinaciones
age = 25
if age >= 18 and age < 65:
    print("Working age")

if age < 18 or age > 65:
    print("Not working age")
```

---

## 🆔 Operadores de Identidad

Verifican si dos variables apuntan al **mismo objeto en memoria**.

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `is` | True si son el mismo objeto | `x is True` |
| `is not` | True si NO son el mismo objeto | `x is not True` |

### Diferencia entre `is` y `==`

#### `is` - Compara identidad (mismo objeto)
```python
a = 5
b = 5
print(a is b)        # True (mismo objeto en memoria)
print(id(a), id(b))  # Mismo ID

# Con listas
list1 = []
list2 = []
print(list1 is list2)     # False (objetos diferentes)
print(id(list1), id(list2))  # IDs diferentes
```

#### `==` - Compara valores (igualdad)
```python
list1 = []
list2 = []
print(list1 == list2)  # True (valores iguales)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True (valores iguales)
print(list1 is list2)  # False (objetos diferentes)
```

### 🔑 Regla Clave
- **`==`** compara **valores** (¿son iguales?)
- **`is`** compara **identidad** (¿son el mismo objeto?)
- Usa `is` principalmente para comparar con `None`: `if x is None:`

---

## 🔍 Operadores de Pertenencia

Verifican si un valor está en una secuencia (string, list, tuple, set, dict).

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `in` | True si el valor está en la secuencia | `5 in x` |
| `not in` | True si el valor NO está en la secuencia | `5 not in x` |

### Ejemplos
```python
# Con listas
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)      # True
print(10 in numbers)     # False
print(10 not in numbers) # True

# Con strings
text = "Python"
print('P' in text)       # True
print('py' in text)      # False (case-sensitive)

# Con diccionarios (solo verifica keys)
person = {'name': 'John', 'age': 30}
print('name' in person)  # True
print('John' in person)  # False (no verifica valores)
```

**Nota**: En diccionarios solo se verifica la presencia de **claves**, no valores.

---

## 📌 Declaración if Simple

```python
if test_expression:
    statement(s)
```

Ejecuta las declaraciones **solo si** la expresión de prueba es `True`.

### Ejemplo
```python
score = 12

if score > 8:
    print("You have passed the exam")

print("Exam was finished.")
```

**Salida:**
```
You have passed the exam
Exam was finished.
```

---

## 📌 Declaración if...else

```python
if expression:
    statement(s)
else:
    statement(s)
```

Ejecuta el bloque `if` si la condición es `True`, de lo contrario ejecuta el bloque `else`.

### Ejemplo
```python
temperature = float(input('What is the temperature? '))

if temperature > 30:
    print('Wear shorts.')
else:
    print('Wear long pants.')

print('Get some exercise outside.')
```

---

## 📌 Declaración if...elif...else

```python
if expression1:
    statement(s)
elif expression2:
    statement(s)
elif expression3:
    statement(s)
else:
    statement(s)
```

- **elif** es abreviatura de "else if"
- Permite verificar **múltiples expresiones**
- Solo se ejecuta **un bloque**
- Puede haber **múltiples elif**, pero solo **un else**

### Ejemplo 1: Clasificación de edad
```python
age = 25

if age < 12:
    print('kid')
elif age < 18:
    print('teenager')
elif age < 50:
    print('adult')
else:
    print('senior')
```

### Ejemplo 2: Sistema de calificaciones
```python
# ❌ Forma anidada (difícil de leer)
if score >= 90:
    letter = 'A'
else:
    if score >= 80:
        letter = 'B'
    else:
        if score >= 70:
            letter = 'C'
        else:
            if score >= 60:
                letter = 'D'
            else:
                letter = 'F'

# ✅ Forma con elif (más clara)
if score >= 90:
    letter = 'A'
elif score >= 80:
    letter = 'B'
elif score >= 70:
    letter = 'C'
elif score >= 60:
    letter = 'D'
else:
    letter = 'F'
```

---

## ❓ Operador Ternario

Sintaxis compacta para if-else en una sola línea.

```python
statement() if condition else statement()
```

### Ejemplos
```python
# Ejemplo 1
weather = "raining"
print("Open Your umbrella" if weather == "raining" else "Wear your cap")
# Output: Open Your umbrella

# Ejemplo 2
result = 'true' if True else 'false'
print(result)  # 'true'

# Ejemplo 3
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # adult
```

---

## 🚫 Python NO soporta switch-case tradicional

**Nota**: Python tradicionalmente NO tenía `switch-case` como otros lenguajes.

---

## 🆕 match...case (Python 3.10+)

Nueva característica en Python 3.10 que funciona como `switch-case`.

### Sintaxis Básica
```python
match status:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not found")
    case _:
        print("Other error")
```

### Características Avanzadas

#### 1. Combinar casos con `|` (OR)
```python
match status:
    case 400:
        print("Bad request")
    case 401 | 403 as error:
        print(f'{error} is authentication error')
    case 404:
        print("Not found")
    case _:
        print("Other error")
```

#### 2. Pattern Matching con parámetros
```python
match values:
    case "load", link:
        load(link)
    case "save", link, filename:
        save(link, filename)
    case "save", link, *filenames:
        for filename in filenames:
            save(link, filename)
    case _:
        default(values)
```

#### 3. Pattern Matching con Arrays
```python
match item:
    case ['evening', action]:
        print(f'You almost finished the day! Now {action}!')
    case [time, action]:
        print(f'Good {time}! It is time to {action}!')
    case _:
        print('The time is invalid.')
```

#### 4. Pattern Matching con Diccionarios
```python
match item:
    case {"time": 'evening', "action": action}:
        print(f'You almost finished the day! Now {action}!')
    case {"time": time, "action": action}:
        print(f'Good {time}! It is time to {action}!')
    case _:
        print('The time is invalid.')
```

#### 5. Pattern Matching con Objetos
```python
class MyClass:
    __match_args__ = ('time', 'action')
    
    def __init__(self, time, action):
        self.time = time
        self.action = action

match item:
    case MyClass(time='evening', action='relax'):
        print(f'You almost finished the day!')
    case MyClass(time, action):
        print(f'Good {time}! It is time to {action}!')
    case _:
        print('The time is invalid.')
```

#### 6. Condiciones adicionales con `if`
```python
match item:
    case ['evening', action] if action not in ['work', 'study']:
        print(f'You almost finished the day! Now {action}!')
    case ['evening', _]:
        print('Come on, you deserve some rest!')
    case [time, action]:
        print(f'Good {time}! It is time to {action}!')
    case _:
        print('The time is invalid.')
```

### Elementos de match...case

- **`_`** : Caso por defecto (catch-all)
- **`|`** : Combinar casos (OR)
- **`as`** : Capturar valor en variable
- **`*`** : Número variable de parámetros
- **`if`** : Agregar condiciones adicionales

---

## 💡 Condiciones Adicionales

### Valores que retornan False
```python
# Colecciones vacías retornan False
a = []
if not a:
    print("List is empty")

# None retorna False
value = None
if not value:
    print("Value is None")

# 0 retorna False
number = 0
if not number:
    print("Number is zero")
```

### Usar `in` para rangos
```python
keyword = "lambda"

if keyword in ["and", "del", "from", "lambda"]:
    print(f"{keyword} is a keyword")
```

### Usar `is` para identidad de objetos
```python
x = y = [1, 2, 3]

print(id(x))    # 4401064560
print(id(y))    # 4401064560
print(x is y)   # True (mismo objeto)

# Comparar con None
value = None
if value is None:
    print("Value is None")
```

---

## ✅ TAREAS

### Ejercicio de Clase 1: Comparador de Números
Escribe un script que determine cuál de dos números ingresados es mayor y cuál es menor. **Considera el caso de igualdad**.

```python
# Ejemplo de entrada/salida:
# Ingresa el primer número: 5
# Ingresa el segundo número: 10
# 10 es mayor que 5
```

---

### Ejercicio de Clase 2: Par o Impar
Escribe un script que verifique si un número ingresado es **par o impar** y muestre el mensaje apropiado.

```python
# Ejemplo:
# Ingresa un número: 7
# 7 es impar
```

---

### Tarea 1: Conversor de Temperatura ⭐

Escribe un programa en Python que:

1. Solicite al usuario ingresar una temperatura en **Celsius**
2. Convierta a **Fahrenheit** usando la fórmula: `F = (C * 9/5) + 32`
3. Imprima la temperatura convertida

**Restricción**: Si el usuario ingresa una temperatura menor a **-273.15°C** (cero absoluto), debe mostrar un mensaje de error en lugar de convertir.

**Nota**: Puedes asumir que el usuario ingresará un número válido.

#### Ejemplo de salida 1:
```
Enter the temperature in Celsius: 25
25°C is equivalent to 77°F
```

#### Ejemplo de salida 2 (error):
```
Enter the temperature in Celsius: -300
Error: Temperature below absolute zero (-273.15°C)
```

---

## 💡 Tips Importantes

1. **Indentación es crucial**: Python usa espacios para definir bloques
2. **Usa elif en lugar de if anidados**: Es más legible
3. **Prefiere `is` para comparar con None**: `if x is None:`
4. **Operador ternario**: Úsalo para condiciones simples en una línea
5. **match...case**: Solo disponible en Python 3.10+
6. **Colecciones vacías son False**: `if not my_list:`
7. **`in` es muy útil**: Para verificar pertenencia en secuencias

---

## 📖 Recursos Adicionales

- [Python if...elif...else - Programiz](https://www.programiz.com/python-programming/if-elif-else)
- [If Statements - Loyola University](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/ifstatements.html)
- [Python match...case - PEP 636](https://peps.python.org/pep-0636/)

---

## 🔑 Resumen Rápido

| Concepto | Sintaxis | Uso |
|----------|----------|-----|
| if simple | `if condition:` | Una condición |
| if-else | `if condition: ... else:` | Dos opciones |
| if-elif-else | `if ... elif ... else:` | Múltiples opciones |
| Ternario | `x if condition else y` | Condición en línea |
| match-case | `match x: case ...:` | Switch (Python 3.10+) |

### Operadores Clave
- **Comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Lógicos**: `and`, `or`, `not`
- **Identidad**: `is`, `is not`
- **Pertenencia**: `in`, `not in`