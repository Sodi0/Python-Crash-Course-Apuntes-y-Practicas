# Funciones en Python

## Conceptos Fundamentales

### ¿Qué es una Función?
Bloque de código organizado y reutilizable que realiza una acción específica. Proporcionan modularidad y reutilización de código.

---

## Definición de Funciones

### Sintaxis Básica
```python
def nombre_funcion(parametros):
    """docstring"""
    # código
    return expresion
```

### Elementos Clave:
- **`def`**: palabra clave para iniciar
- **Paréntesis `()`**: contienen parámetros
- **Docstring `""" """`**: documentación (opcional pero recomendado)
- **`:`**: inicia el bloque de código
- **Indentación**: define el cuerpo de la función
- **`return`**: devuelve un valor (si no hay return, devuelve `None`)

### Ejemplo:
```python
def saludar(nombre):
    """Saluda a la persona"""
    return "Hola, " + nombre
```

---

## Tipos de Argumentos

### 1. **Argumentos Requeridos (Posicionales)**
```python
def imprimir(texto):
    print(texto)

imprimir("Hola")  # ✓ Correcto
imprimir()        # ✗ Error: falta argumento
```

### 2. **Argumentos por Defecto**
```python
def info(nombre, edad=18):
    print(f"Nombre: {nombre}, Edad: {edad}")

info("Alex")        # Usa edad=18 por defecto
info("Ana", 25)     # Sobrescribe el valor por defecto
```

### 3. **Argumentos por Palabra Clave (Keyword)**
```python
def info(nombre, edad):
    print(f"{nombre}: {edad}")

info(edad=30, nombre="Alex")  # Orden no importa
```

⚠️ **Importante**: No puedes poner argumentos posicionales después de keyword arguments.

### 4. **Argumentos Variables (*args)**
```python
def sumar(primero, *numeros):
    total = primero
    for num in numeros:
        total += num
    return total

sumar(1, 2, 3, 4, 5)  # Acepta cualquier cantidad
```

---

## 🌐 Scope y Lifetime de Variables

### Variables Locales vs Globales

**Local**: Declarada dentro de la función
```python
def funcion():
    x = 10  # Local - solo existe dentro de la función
```

**Global**: Declarada fuera de la función
```python
x = 20  # Global - accesible desde cualquier lugar

def funcion():
    print(x)  # Puede leer la variable global
```

### Keyword `global`
Para **modificar** una variable global dentro de una función:
```python
contador = 0

def incrementar():
    global contador  # Necesario para modificar
    contador += 1
```

### Keyword `nonlocal`
Para variables en funciones anidadas:
```python
def exterior():
    x = 10
    def interior():
        nonlocal x  # Accede a x de la función exterior
        x = 20
```

---

## 🔄 Recursión

### Concepto
Función que se llama a sí misma. Debe tener:
1. **Caso base**: condición de parada
2. **Caso recursivo**: llamada a sí misma

### Ejemplo: Factorial
```python
def factorial(n):
    if n == 1:        # Caso base
        return 1
    return n * factorial(n-1)  # Caso recursivo

factorial(3)  # 3 * 2 * 1 = 6
```

### Ventajas vs Desventajas
✅ Código elegante y limpio  
✅ Simplifica problemas complejos  
❌ Consume más memoria  
❌ Puede ser difícil de depurar  

---

## λ Funciones Lambda (Anónimas)

### Sintaxis
```python
lambda argumentos: expresion
```

### Características:
- Una sola expresión
- Retorno implícito
- Sin nombre
- Uso temporal

### Ejemplos:
```python
# Función normal
def cuadrado(x):
    return x ** 2

# Equivalente lambda
cuadrado = lambda x: x ** 2

# Uso con filter/map
numeros = [1, 2, 3, 4]
pares = list(filter(lambda x: x % 2 == 0, numeros))
```

---

## 🎯 Puntos Clave para Recordar

1. **Docstrings**: Siempre documenta tus funciones con `"""texto"""`
2. **Return**: Sin return explícito, la función devuelve `None`
3. **Scope**: Variables locales no existen fuera de la función
4. **`*args`**: Para número variable de argumentos
5. **Lambda**: Útil para funciones simples de una línea
6. **Recursión**: Siempre define un caso base para evitar loops infinitos


---