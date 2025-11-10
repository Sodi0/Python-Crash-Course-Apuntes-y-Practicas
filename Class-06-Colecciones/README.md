# Apuntes: Colecciones en Python

## Tipos de Colecciones

Python tiene 4 tipos principales de colecciones:

1. **List**: Ordenada, modificable, permite duplicados
2. **Tuple**: Ordenada, inmutable, permite duplicados
3. **Set**: No ordenada, no indexada, sin duplicados
4. **Dictionary**: No ordenada, modificable, indexada, sin claves duplicadas

---

## LISTAS (List)

### Características
- Secuencia ordenada de elementos
- Elementos pueden ser de diferentes tipos
- Mutables (se pueden modificar)
- Dinámicas (el tamaño puede cambiar)
- Se escriben entre corchetes `[]`

### Creación
```python
mylist = [1, 2, 3, 4, 5]
mixed_list = [True, "hello", 3.14, [1, 2]]
```

### Operaciones Principales
- **Indexing**: Acceso por índice `mylist[0]`
- **Negative indexing**: Acceso desde el final `mylist[-1]`
- **Slicing**: `mylist[start:stop:step]`
- **Concatenación**: `list1 + list2`
- **Repetición**: `list * 3`
- **Membership**: `item in list`

### Métodos Importantes
- `append(x)`: Añade elemento al final
- `insert(i, x)`: Inserta en posición específica
- `remove(x)`: Elimina el primer elemento con valor x
- `pop(i)`: Elimina y retorna elemento en posición i
- `clear()`: Elimina todos los elementos
- `index(x)`: Retorna índice del primer elemento x
- `count(x)`: Cuenta ocurrencias de x
- `sort()`: Ordena la lista in-place
- `reverse()`: Invierte el orden in-place
- `copy()`: Retorna copia superficial
- `extend(iterable)`: Añade elementos de un iterable

### Funciones Built-in
- `len()`: Longitud de la lista
- `max()`, `min()`: Máximo y mínimo
- `sum()`: Suma de elementos
- `sorted()`: Retorna nueva lista ordenada (no modifica original)
- `all()`: True si todos los elementos son verdaderos
- `any()`: True si algún elemento es verdadero
- `enumerate()`: Retorna objeto enumerate con índices

### List Comprehension
Forma elegante de crear listas:
```python
# Básico
pow2 = [2 ** x for x in range(10)]

# Con filtro
odd = [x for x in range(20) if x % 2 == 1]

# Anidado
[x+y for x in ['Python ','C '] for y in ['Language','Programming']]
```

### Iteración
```python
for item in mylist:
    print(item)

for i in range(len(mylist)):
    print(mylist[i])
```

---

## TUPLAS (Tuple)

### Características
- Similar a las listas pero **inmutables**
- Una vez creadas no se pueden modificar
- Se escriben con paréntesis `()` o solo con comas
- Más eficientes en memoria que las listas

### Creación
```python
mytuple = (1, 2, 3)
mytuple = 1, 2, 3  # También válido
single = (1,)  # Tupla de un elemento (nota la coma)
```

### Acceso a Elementos
Mismo comportamiento que listas:
- Indexing
- Negative indexing
- Slicing

### Métodos (solo 2)
- `count(x)`: Cuenta ocurrencias de x
- `index(x)`: Retorna índice de la primera ocurrencia de x

### Funciones Built-in
- `all()`, `any()`, `enumerate()`, `len()`, `max()`, `min()`, `sorted()`, `sum()`, `tuple()`

### Modificación
No se puede cambiar directamente, pero se puede:
- Convertir a lista, modificar y volver a tupla
- Crear nueva tupla

### Eliminación
```python
del mytuple  # Elimina la tupla completa
```

---

## SETS (Conjunto)

### Características
- Colección **no ordenada** y **no indexada**
- **Sin elementos duplicados**
- Se escribe con llaves `{}`
- Útil para operaciones matemáticas de conjuntos

### Creación
```python
myset = {1, 2, 3, 4, 5}
emptyset = set()  # Set vacío (no usar {})
```

### Métodos de Modificación
- `add(x)`: Añade un elemento
- `update([list])`: Añade múltiples elementos
- `remove(x)`: Elimina x (error si no existe)
- `discard(x)`: Elimina x (sin error si no existe)
- `pop()`: Elimina y retorna elemento aleatorio
- `clear()`: Elimina todos los elementos

### Operaciones de Conjuntos
- **Unión**: `set1 | set2` o `set1.union(set2)`
- **Intersección**: `set1 & set2` o `set1.intersection(set2)`
- **Diferencia**: `set1 - set2` o `set1.difference(set2)`
- **Diferencia Simétrica**: `set1 ^ set2` o `set1.symmetric_difference(set2)`

### Funciones Built-in
- `len()`, `max()`, `min()`, `sum()`, `sorted()`, `all()`, `any()`, `enumerate()`

### Frozenset
Versión inmutable del set:
```python
fs = frozenset([1, 2, 3])
```
Soporta métodos como `copy()`, `difference()`, `intersection()`, etc., pero no métodos que añadan/eliminen elementos.

---

## DICCIONARIOS (Dictionary)

### Características
- Colección **no ordenada** de pares clave-valor
- Las claves deben ser **inmutables** y **únicas**
- Los valores pueden ser cualquier objeto y repetirse
- Se escriben con llaves `{}` con pares `key: value`

### Creación
```python
mydict = {'name': 'John', 'age': 30, 'city': 'Madrid'}
mydict = dict(name='John', age=30, city='Madrid')
```

### Acceso a Elementos
```python
value = mydict['key']  # Error si no existe
value = mydict.get('key')  # Retorna None si no existe
value = mydict.get('key', default_value)  # Retorna default si no existe
```

### Métodos Principales
- `clear()`: Elimina todos los items
- `copy()`: Retorna copia superficial
- `get(key, default)`: Obtiene valor de key
- `items()`: Retorna vista de pares (key, value)
- `keys()`: Retorna vista de las claves
- `values()`: Retorna vista de los valores
- `pop(key)`: Elimina y retorna valor de key
- `popitem()`: Elimina y retorna par (key, value) arbitrario
- `update(dict)`: Actualiza con pares de otro diccionario
- `setdefault(key, default)`: Retorna valor o lo inserta si no existe
- `fromkeys(seq, value)`: Crea dict con keys de seq

### Dictionary Comprehension
```python
squares = {x: x*x for x in range(6)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Con condición
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
```

### Iteración
```python
# Por claves (default)
for key in mydict:
    print(key, mydict[key])

# Por pares clave-valor
for key, value in mydict.items():
    print(key, value)

# Solo claves
for key in mydict.keys():
    print(key)

# Solo valores
for value in mydict.values():
    print(value)
```

### Membership Test
```python
'name' in mydict  # True si la clave existe
```

### Funciones Built-in
- `len()`: Número de pares
- `sorted()`: Lista ordenada de claves
- `all()`: True si todas las claves son verdaderas
- `any()`: True si alguna clave es verdadera

---

## Funciones Comunes Importantes

### `all(iterable)`
Retorna True si todos los elementos son verdaderos (o si está vacío)
```python
all([True, True, True])  # True
all([0, 1, 1])  # False (0 es falsy)
```

### `any(iterable)`
Retorna True si algún elemento es verdadero
```python
any([False, True, False])  # True
any([0, 0, 0])  # False
```

### `enumerate(iterable, start=0)`
Añade contador a un iterable
```python
list(enumerate(['a', 'b', 'c']))
# [(0, 'a'), (1, 'b'), (2, 'c')]
```

---

## Resumen de Cuándo Usar Cada Tipo

- **List**: Cuando necesitas una colección ordenada y modificable
- **Tuple**: Para datos que no deben cambiar, más eficiente
- **Set**: Para eliminar duplicados o realizar operaciones matemáticas de conjuntos
- **Dictionary**: Para mapear claves a valores, búsquedas rápidas por clave