# Resumen OOP en Python - Puntos Clave

## Conceptos Fundamentales

### Clase y Objeto
- **Clase**: Plantilla o prototipo para crear objetos
- **Objeto**: Colección de datos (variables) y métodos (funciones) que actúan sobre esos datos
- **Instanciación**: Proceso de crear un objeto a partir de una clase
- **Todo en Python es un objeto**

### Principios de OOP
1. **Herencia**: Usar detalles de una clase existente sin modificarla
2. **Encapsulación**: Ocultar detalles privados de una clase
3. **Polimorfismo**: Usar operaciones comunes de diferentes formas para diferentes datos

## Sintaxis Básica de Clases

```python
class ClassName:
    '''Docstring'''
    # Atributos y métodos
    pass
```

### Nomenclatura
- **Atributos**: Miembros de la clase
- **Métodos**: Funciones de la clase
- **Propiedades**: Campos de la clase

## Constructor y Métodos Especiales

### `__init__()` - Constructor
- Se llama automáticamente al crear un objeto
- Inicializa las variables del objeto
- **self** siempre es el primer parámetro (referencia al objeto mismo)

```python
class Person:
    def __init__(self, name):
        self.name = name
```

### `__del__()` - Destructor
- Se llama al eliminar un objeto
- Python tiene gestión automática de memoria

### Otros Métodos Especiales
- `__str__()`: Representación imprimible del objeto
- `__repr__()`: Representación evaluable del objeto
- `__add__()`, `__sub__()`, etc.: Sobrecarga de operadores

## Parámetro self

**MUY IMPORTANTE**: 
- `firstobject.func()` se traduce internamente a `MyClass.func(firstobject)`
- El objeto siempre se pasa como primer argumento
- Convención obligatoria en la comunidad Python

## Variables de Clase vs Instancia

### Variables de Instancia
- Únicas para cada objeto
- Se definen con `self.variable`
- Valores diferentes en cada instancia

### Variables de Clase (Estáticas)
- Compartidas por todos los objetos
- Se definen directamente en la clase
- Útiles para contadores, configuraciones compartidas

```python
class Account:
    counter = 0  # Variable de clase
    
    def __init__(self, holder):
        Account.counter += 1
        self.holder = holder  # Variable de instancia
```

## Tipos de Métodos

### 1. Métodos de Instancia
- Parámetro: `self`
- Acceden y modifican el estado del objeto
- Pueden modificar el estado de la clase vía `self.__class__`

### 2. Métodos de Clase (`@classmethod`)
- Parámetro: `cls`
- Solo modifican el estado de la clase
- No pueden modificar instancias individuales

### 3. Métodos Estáticos (`@staticmethod`)
- Sin `self` ni `cls`
- No modifican estado de objeto ni clase
- Principalmente para organización/namespace

## Encapsulación - Niveles de Acceso

| Nomenclatura | Tipo | Acceso |
|--------------|------|--------|
| `name` | Público | Desde cualquier lugar |
| `_name` | Protegido | Convención: no acceder directamente desde fuera |
| `__name` | Privado | No accesible desde fuera (name mangling: `_ClassName__name`) |

### Property (Getters/Setters)

```python
class P:
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        if value < 0:
            self.__x = 0
        else:
            self.__x = value
```

## Herencia

### Herencia Simple
```python
class Child(Parent):
    def __init__(self):
        super().__init__()  # Llamar constructor del padre
```

### Herencia Múltiple
- Python permite heredar de múltiples clases
- Orden de búsqueda de métodos: **MRO (Method Resolution Order)**
- Búsqueda: depth-first, left-right

### Method Overriding
- La clase hija puede sobrescribir métodos del padre
- Usar `super()` para extender (no reemplazar) funcionalidad del padre

### Funciones Útiles
- `isinstance(obj, Class)`: Verifica si obj es instancia de Class
- `issubclass(Child, Parent)`: Verifica herencia entre clases

## Sobrecarga de Operadores

### Operadores Aritméticos
- `+` → `__add__(self, other)`
- `-` → `__sub__(self, other)`
- `*` → `__mul__(self, other)`
- `/` → `__truediv__(self, other)`
- `//` → `__floordiv__(self, other)`
- `%` → `__mod__(self, other)`
- `**` → `__pow__(self, other)`

### Operadores de Comparación
- `<` → `__lt__(self, other)`
- `<=` → `__le__(self, other)`
- `==` → `__eq__(self, other)`
- `!=` → `__ne__(self, other)`
- `>` → `__gt__(self, other)`
- `>=` → `__ge__(self, other)`

## Polimorfismo

**Concepto**: Usar la misma interfaz para diferentes formas de datos

```python
class Rectangle:
    def draw(self):
        print("Drawing rectangle")

class Circle:
    def draw(self):
        print("Drawing circle")

# Misma interfaz, diferente implementación
```

## Conceptos Avanzados

### Método `__new__`
- Se llama ANTES de `__init__`
- Controla la creación de la instancia
- Útil para patrones como Singleton

### Singleton Pattern
```python
class Singleton:
    obj = None
    
    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = object.__new__(cls)
        return cls.obj
```

## Principio DRY
**Don't Repeat Yourself**: OOP facilita la reutilización de código

---

## Puntos Clave para Recordar

- **self** es obligatorio como primer parámetro en métodos de instancia  
- Todo en Python hereda de la clase `object`  
- Usar `super()` para llamar métodos del padre  
- Variables con `__` son privadas (name mangling)  
- `@property` para crear getters/setters pythónicos  
- MRO define el orden de búsqueda en herencia múltiple  
- Métodos especiales (`__init__`, `__str__`, etc.) definen comportamiento de objetos