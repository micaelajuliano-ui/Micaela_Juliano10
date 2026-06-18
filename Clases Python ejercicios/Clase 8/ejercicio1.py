import math

def combinaciones(fichas):
    cantidad_fichas = len(fichas)
    return math.factorial(cantidad_fichas)

fichas = ['A', 'B', 'C']
print(f"Cantidad de combinaciones posibles para las fichas {fichas}: {combinaciones(fichas)}")

