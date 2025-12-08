from math import pi, pow

def area_circulo(radio):
    return pi * pow(radio, 2)

def area_triangulo(base, altura):
    return 0.5 * base * altura

def area_rectangulo(base, altura):
    return base * altura