class Humano:
    especie = "Homo sapiens"

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."
    
    @classmethod
    def homosapiens(cls):
        return f"Todos los humanos pertenecen a la especie {cls.especie}."

    @staticmethod
    def mensaje_estatico():
        return "Este es un mensaje estático de la clase Humano."
    
