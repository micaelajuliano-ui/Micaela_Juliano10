import math

def calcular_raices(a, b, c):
    discriminante = b**2 - 4*a*c
    
    if discriminante < 0:
        return "Las raíces son imaginarias."
    
    raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
    
    return raiz1, raiz2

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))

raices = calcular_raices(a, b, c)

print(f"Las raíces de la función cuadrática son: {raices}")

