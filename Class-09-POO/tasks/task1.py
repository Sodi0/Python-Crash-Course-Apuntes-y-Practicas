# Task 1
class Poligono:
    def __init__(self, lados):
        self.lados = lados

class Rectangulo(Poligono):
    def __init__(self, lados, base, altura):
        super().__init__(lados)
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
# Crear una instancia de Rectangulo y mostrar sus lados y área
rectangulo = Rectangulo(4, 5, 10)
print(f"Lados: {rectangulo.lados}")
print(f"Area: {rectangulo.area()}")