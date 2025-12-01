# Apuntes: Manejo de Excepciones en Python

## 🔑 Conceptos Fundamentales

### Errores vs Excepciones
- **Errores de Sintaxis**: Ocurren al escribir el código, antes de la compilación
  - El IDE puede detectarlos automáticamente
  - Ejemplo: `print( 0 / 0 ))`
  
- **Excepciones**: Errores en tiempo de ejecución
  - Aparecen cuando el programa ya está corriendo
  - Python genera un objeto de tipo Exception
  - Pueden ser manejadas para evitar que el programa se cierre

## 📊 Jerarquía de Excepciones

```
BaseException
└── Exception
    ├── ArithmeticError
    │   └── ZeroDivisionError
    ├── IOError
    ├── IndexError
    ├── KeyError
    ├── NameError
    ├── TypeError
    ├── ValueError
    └── ...
```

## 🎯 Excepciones Estándar Más Comunes

| Excepción | Cuándo ocurre |
|-----------|---------------|
| **ZeroDivisionError** | División por cero |
| **IndexError** | Índice fuera de rango en secuencias |
| **KeyError** | Clave no encontrada en diccionario |
| **NameError** | Variable no definida |
| **TypeError** | Operación inválida para el tipo de dato |
| **ValueError** | Argumento con valor inválido |
| **IOError** | Error en operaciones de entrada/salida |
| **ImportError** | Módulo no encontrado |

## 🛡️ Manejo de Excepciones

### Sintaxis Básica: try-except
```python
try:
    # código que puede generar error
    print(a[4])
except IndexError as e:
    print(e)
```

### Múltiples Excepciones

**Opción 1: Una sola cláusula**
```python
except(ZeroDivisionError, NameError, ValueError):
    print("Error Occurred and Handled")
```

**Opción 2: Cláusulas separadas** (⭐ Más específico)
```python
except ValueError:
    print("Value Error!")
except NameError:
    print("NameError!")
except ZeroDivisionError:
    print("ZeroDivisionError!")
except:
    print("Error genérico!")
```

### Bloques else y finally

```python
try:
    # código que puede fallar
    f.write("texto")
except:
    print("Error al escribir")
else:
    # se ejecuta solo si NO hubo error
    print("Todo OK")
finally:
    # SIEMPRE se ejecuta
    f.close()
```

## 🚀 Lanzar Excepciones (raise)

Puedes generar excepciones manualmente:

```python
try:
    value = int(input("Enter a positive integer: "))
    if value <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as e:
    print(e)
```

## 🎨 Excepciones Personalizadas

```python
class CustomError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

# Uso
try:
    if num_of_group < 1:
        raise CustomError("Number can't be less than 1")
except CustomError as e:
    print("Error:", e.data)
```

## 📝 Logging

### Niveles de Severidad (de menor a mayor)
1. **DEBUG** - Información detallada para diagnóstico
2. **INFO** - Confirmación de funcionamiento normal
3. **WARNING** - Advertencia de problemas potenciales
4. **ERROR** - Error que impide alguna funcionalidad
5. **CRITICAL** - Error crítico que puede detener el programa

### Configuración Básica

```python
import logging

# Configurar
logging.basicConfig(
    filename='app.log',
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

# Usar
logging.warning('This will get logged to a file')
```

### Capturar Stack Traces

```python
try:
    c = a / b
except Exception as e:
    logging.exception("Exception occurred")  # Incluye stack trace
```

### Logger Personalizado

```python
logger = logging.getLogger('Example_logger')
logger.warning('This is a warning')
```

## ⚠️ Mejores Prácticas

1. ✅ Captura excepciones específicas, evita `except:` genérico
2. ✅ Usa `else` para código que debe ejecutarse solo si no hay errores
3. ✅ Usa `finally` para limpieza (cerrar archivos, conexiones)
4. ✅ Implementa logging para producción en lugar de `print()`
5. ✅ Crea excepciones personalizadas para lógica de negocio específica

---

**Punto clave**: El manejo de excepciones permite que tu programa sea robusto y maneje situaciones inesperadas de manera elegante, en lugar de simplemente cerrarse.
 
> "Explicit is better than implicit" - Zen of Python