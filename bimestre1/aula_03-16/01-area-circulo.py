import math

def calcular_area_do_circulo(r):
    return math.pi * (r**2)

r = int(input("Insira o valor do raio: "))
print(f"Área: {calcular_area_do_circulo(r):.2f}")