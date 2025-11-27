class Empleado:
    """Clase que representa a un empleado con nombre, apellido y salario."""
    total_empleados = 0

    def __init__(self, nombre, apellido, salario):
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario
        Empleado.total_empleados += 1

    def mostrar_detalles(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Salario: {self.salario}"
    
    @classmethod
    def contar_empleados(cls):
        return f"Total de empleados: {cls.total_empleados}"
    
# Crear instancias de empleado y mostrar detalles
empleado1 = Empleado("Juan", "Pérez", 50000)
empleado2 = Empleado("Ana", "Gómez", 60000) 
print(empleado1.mostrar_detalles())
print(empleado2.mostrar_detalles())
print(Empleado.contar_empleados())

#mostrar informacion de la clase empleado
print("Información de la clase empleado:")
print(Empleado.__base__)
print(Empleado.__dict__)
print(Empleado.__name__)
print(Empleado.__module__)
print(Empleado.__doc__)