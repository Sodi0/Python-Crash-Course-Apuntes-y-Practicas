class Bus:
    def __init__(self, marca, anio, kilometraje, placa, ruta):
        self.marca = marca
        self.anio = anio
        self.kilometraje = kilometraje
        self.placa = placa
        self.ruta = ruta

    def antiguedad(self):
        if self.anio >= 2022:
            return "nuevo"
        elif self.anio >= 2015 and self.anio < 2021:
            return "reciente"
        elif self.anio >= 2005 and self.anio <= 2014:
            return "común"
        elif self.anio < 2005:
            return "antiguo"
        
    def origen(self):
        if self.marca.lower() in ["scania", "volvo", "daimler", "man"]:
            return "europeo"
        else:
            return "otro"
        

b = Bus("Daimler", 2004, 800000, "ERG963", "250")
#print(b.antiguedad())
#print(b.origen())

# Question 2
class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __add__(self, otro):
        real_resultado = self.real + otro.real
        imaginario_resultado = self.imaginario + otro.imaginario
        return Complejo(real_resultado, imaginario_resultado)

    def __sub__(self, otro):
        real_resultado = self.real - otro.real
        imaginario_resultado = self.imaginario - otro.imaginario
        return Complejo(real_resultado, imaginario_resultado)

    def mostrar(self):
        return f"{self.real} + {self.imaginario}i"
    
c1 = Complejo(1, 1)
c2 = Complejo(1, 1)
complejo_suma = c1 + c2
complejo_resta = c1 - c2
print(complejo_suma.real)
print(complejo_suma.imaginario)
print(complejo_resta.real)
print(complejo_resta.imaginario)

# Question 3
class Cubo:
    def __init__(self, lado):
        self.lado = lado

    def volumen(self):
        return self.lado ** 3
    
    def area(self):
        return 6 * (self.lado ** 2)
    
c = Cubo(12)
#print(c.volumen())
#print(c.area())

# Question 4
class Calculadora:
    def __init__(self):
        pass

    def sumar(self, numero1, numero2):
        return numero1 + numero2

    def restar(self, numero1, numero2):
        return numero1 - numero2

    def multiplicar(self, numero1, numero2):
        return numero1 * numero2

    def dividir(self, numero1, numero2):
        if numero2 != 0:
            return numero1 / numero2
        else:
            return "Error: División por cero"
        
c = Calculadora()
#print(c.sumar(87, -125))
#print(c.restar(24, -87))
#print(c.multiplicar(7, -6))
#print(c.dividir(40, -20))