import math

def areaCirculo(radio):
    area = math.pi * radio ** 2
    return area

radioRecibido = int(input("Ingrese el radio del círculo: "))
print(f"El área del círculo es: {areaCirculo(radioRecibido)}")

