# Loops en Python

## 📋 Agenda
- Bucle `while`
- Bucle `for`
- Función `range()`
- Declaraciones `break`, `continue` y `pass`

---

## 🔄 while Loop

Ejecuta un bloque de código **mientras** una condición sea verdadera.

### Sintaxis
```python
while expression:
    suite
[else:
    suite]
```

### Características
- Evalúa la expresión **antes** de cada iteración
- El bloque `else` es **opcional** y se ejecuta cuando la condición se vuelve `False`
- Si la condición es `False` desde el inicio, el bucle no se ejecuta

### Ejemplo Básico
```python
start = 0
finish = 10

while start < finish:
    print(start)
    start += 1
else:
    print("The end")
```

**Salida:**
```
0
1
2
3
4
5
6
7
8
9
The end
```

### Ejemplo con contador
```python
count = 0

while count < 5:
    print(f"Count is: {count}")
    count += 1

print("Loop finished")
```

### ⚠️ Cuidado con bucles infinitos
```python
# ❌ Bucle infinito - nunca termina
while True:
    print("This will run forever")

# ✅ Bucle con condición de salida
counter = 0
while True:
    print(counter)
    counter += 1
    if counter >= 5:
        break
```

---

## 🔁 for Loop

Itera sobre una **secuencia** (lista, tupla, string, etc.) o cualquier objeto iterable.

### Sintaxis
```python
for target_list in expression_list:
    suite
[else:
    suite]
```

### Características
- Itera sobre cada elemento de la secuencia
- El bloque `else` es **opcional** y se ejecuta al terminar el bucle normalmente
- Más eficiente que `while` cuando conoces el número de iteraciones

### Ejemplo con Lista
```python
for j in [0, 1, 2, 3, 4]:
    print(j)
else:
    print(f"{j} - is the last")
```

**Salida:**
```
0
1
2
3
4
4 - is the last
```

### Ejemplo con String
```python
for letter in "Python":
    print(letter)
```

**Salida:**
```
P
y
t
h
o
n
```

### Ejemplo con Diccionario
```python
person = {'name': 'John', 'age': 30, 'city': 'New York'}

# Iterar sobre keys
for key in person:
    print(key)

# Iterar sobre values
for value in person.values():
    print(value)

# Iterar sobre items (key-value pairs)
for key, value in person.items():
    print(f"{key}: {value}")
```

---

## 🔢 Función range()

Genera una secuencia de números. Muy útil con bucles `for`.

### Sintaxis
```python
range(stop)                    # De 0 a stop-1
range(start, stop)             # De start a stop-1
range(start, stop, step)       # De start a stop-1, incrementando step
```

### Ejemplos

#### 1. range(stop)
```python
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(5):
    print(i)
# 0, 1, 2, 3, 4
```

#### 2. range(start, stop)
```python
print(list(range(5, 10)))
# [5, 6, 7, 8, 9]

for i in range(3, 7):
    print(i)
# 3, 4, 5, 6
```

#### 3. range(start, stop, step)
```python
print(list(range(0, 10, 2)))
# [0, 2, 4, 6, 8]

# Números impares
for i in range(1, 10, 2):
    print(i)
# 1, 3, 5, 7, 9

# Cuenta regresiva
print(list(range(10, 0, -1)))
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### 🔑 Puntos Clave sobre range()
- Retorna un objeto range (no una lista)
- Es **eficiente en memoria** (genera números bajo demanda)
- El valor `stop` **NO se incluye**
- `step` puede ser negativo para contar hacia atrás

---

## 🛑 Declaración break

Termina el bucle **inmediatamente**, sin ejecutar el bloque `else`.

### Sintaxis
```python
for val in sequence:
    if condition:
        break
    # más código
```

### Ejemplo
```python
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")
```

**Salida:**
```
s
t
r
The end
```

### Uso Común: Búsqueda
```python
numbers = [1, 3, 5, 7, 8, 10]

for num in numbers:
    if num % 2 == 0:
        print(f"First even number found: {num}")
        break
else:
    print("No even numbers found")
```

---

## ⏭️ Declaración continue

Salta el resto de la **iteración actual** y continúa con la siguiente.

### Sintaxis
```python
for val in sequence:
    if condition:
        continue
    # este código se salta si condition es True
```

### Ejemplo
```python
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")
```

**Salida:**
```
s
t
r
n
g
The end
```

### Diferencia entre break y continue

```python
# break - termina el bucle
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0, 1, 2, 3, 4

# continue - salta a la siguiente iteración
for i in range(10):
    if i == 5:
        continue
    print(i)
# Output: 0, 1, 2, 3, 4, 6, 7, 8, 9 (salta el 5)
```

---

## ⏸️ Declaración pass

No hace nada. Es un **placeholder** (marcador de posición).

### ¿Cuándo usar pass?

- Cuando necesitas un bloque sintácticamente pero no quieres ejecutar código
- Como placeholder para funcionalidad futura
- Python no permite bloques vacíos

### Sintaxis
```python
for val in sequence:
    pass  # TODO: implementar lógica después
```

### Ejemplos

#### Con bucle
```python
sequence = {'p', 'a', 's', 's'}

for val in sequence:
    pass  # No hace nada, pero es sintácticamente correcto
```

#### Con if
```python
x = 10

if x > 5:
    pass  # TODO: agregar lógica aquí
else:
    print("x es pequeño")
```

#### Con función
```python
def my_function():
    pass  # Implementar después

def calculate_tax(amount):
    pass  # TODO: agregar cálculo de impuestos
```

#### Con clase
```python
class MyClass:
    pass  # Clase vacía por ahora
```

---

## 🔄 Comparación: while vs for

| Característica | while | for |
|----------------|-------|-----|
| **Uso** | Cuando no conoces iteraciones | Cuando conoces iteraciones |
| **Condición** | Se evalúa cada vez | Itera sobre secuencia |
| **Riesgo** | Bucle infinito si olvidas actualizar | Más seguro |
| **Ejemplo** | Leer hasta EOF | Iterar sobre lista |

### Cuándo usar cada uno

#### Usa `while` cuando:
- No sabes cuántas iteraciones necesitas
- Esperas input del usuario
- La condición es compleja

```python
# Ejemplo: input del usuario
password = ""
while password != "1234":
    password = input("Enter password: ")
```

#### Usa `for` cuando:
- Iteras sobre una colección
- Conoces el rango de iteraciones
- Quieres código más legible

```python
# Ejemplo: procesar lista
names = ['Alice', 'Bob', 'Charlie']
for name in names:
    print(f"Hello, {name}!")
```

---

## 📚 Bloque else en Loops

Tanto `while` como `for` pueden tener un bloque `else`.

### Comportamiento
- Se ejecuta cuando el bucle **termina normalmente**
- **NO** se ejecuta si el bucle termina con `break`

### Ejemplo con for
```python
# else se ejecuta
for i in range(5):
    print(i)
else:
    print("Loop completed normally")

# else NO se ejecuta (hay break)
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")
```

### Uso Práctico: Búsqueda
```python
numbers = [1, 3, 5, 7, 9]

for num in numbers:
    if num % 2 == 0:
        print("Found even number")
        break
else:
    print("No even numbers found")  # Se ejecuta si no hay break
```

---

## ✅ EJERCICIOS DE CLASE

### Ejercicio 1: Números Pares
Imprime todos los números pares menores que 100.  
**Escribe DOS versiones:**
1. Usando bucle `while`
2. Usando bucle `for`

```python
# Versión con while
# Tu código aquí

# Versión con for
# Tu código aquí
```

---

### Ejercicio 2: Números Impares
Imprime todos los números impares menores que 100.  
**Escribe DOS versiones:**
1. Usando el operador `continue`
2. Sin usar `continue`

```python
# Versión con continue
# Tu código aquí

# Versión sin continue
# Tu código aquí
```

---

### Ejercicio 3: Detectar Números Impares
Verifica si una lista contiene números impares.  
**Pista:** Usa la declaración `break` para terminar cuando encuentres el primer impar.

```python
numbers = [2, 4, 6, 8, 9, 10]
# Tu código aquí
```

---

## ✅ TAREAS

### Tarea 1: Conversión de Tipos ⭐

Crea una lista que contenga elementos de tipo entero, luego usa un bucle para **cambiar el tipo** de estos elementos a tipo flotante.

**Pista:** Usa la función `float()`.

**Ejemplo:**
```python
# Input
my_list = [1, 2, 3, 4, 5]

# Tu código aquí

# Output esperado
# [1.0, 2.0, 3.0, 4.0, 5.0]
```

---

### Tarea 2: Secuencia de Fibonacci ⭐⭐

Imprime los números de Fibonacci hasta el número **n** ingresado, usando bucles.

**Secuencia de Fibonacci:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

**Regla:** Cada número es la suma de los dos anteriores.

**Ejemplo de ejecución:**
```python
# Input
Enter n: 50

# Output esperado
0
1
1
2
3
5
8
13
21
34
```

**Pista:** 
- Necesitas dos variables para almacenar los dos números anteriores
- Usa un bucle `while` para continuar hasta que el siguiente número supere `n`

---

## 💡 Tips Importantes

1. **Evita bucles infinitos**: Siempre asegúrate que la condición cambie
2. **range() no incluye el stop**: `range(5)` va de 0 a 4
3. **break termina el bucle**: `else` no se ejecuta con `break`
4. **continue salta iteración**: El resto del código en esa iteración se omite
5. **pass es un placeholder**: Útil durante desarrollo
6. **for es más "pythonic"**: Prefiérelo cuando sea posible
7. **enumerate() es útil**: Cuando necesitas índice y valor
   ```python
   for index, value in enumerate(['a', 'b', 'c']):
       print(f"{index}: {value}")
   ```

---

## 🎯 Patrones Comunes

### Iterar con índice
```python
# ❌ No pythonic
for i in range(len(my_list)):
    print(my_list[i])

# ✅ Pythonic
for item in my_list:
    print(item)

# ✅ Si necesitas índice
for i, item in enumerate(my_list):
    print(f"{i}: {item}")
```

### Iterar sobre múltiples listas
```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### Crear lista con comprensión (avanzado)
```python
# En lugar de:
squares = []
for i in range(10):
    squares.append(i ** 2)

# Usa list comprehension:
squares = [i ** 2 for i in range(10)]
```

---

## 📖 Recursos Adicionales

- [Python Loops - W3Schools](https://www.w3schools.com/python/python_for_loops.asp)
- [Python range() - Real Python](https://realpython.com/python-range/)
- [Python break, continue, pass - Programiz](https://www.programiz.com/python-programming/break-continue)

---

## 🔑 Resumen Rápido

| Concepto | Propósito | Cuándo Usar |
|----------|-----------|-------------|
| `while` | Repite mientras condición es True | No sabes # de iteraciones |
| `for` | Itera sobre secuencia | Conoces la secuencia/rango |
| `range()` | Genera secuencia de números | Con bucles for |
| `break` | Termina el bucle | Encontraste lo que buscabas |
| `continue` | Salta a siguiente iteración | Omitir casos específicos |
| `pass` | No hace nada | Placeholder para código futuro |
| `else` (en loop) | Ejecuta si loop termina normal | Verificar si se usó break |

### Flujo de Control

```
while condition:
    if break_condition:
        break          # Sale del bucle
    if skip_condition:
        continue       # Salta a siguiente iteración
    # código normal
else:
    # Solo si NO hubo break
```