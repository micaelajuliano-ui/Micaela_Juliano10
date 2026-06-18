temperaturas = [15, 20, 22, 18, 25, 30, 28, 27, 26, 24, 19, 21, 23, 17, 16, 14, 13, 12, 11, 10, -2, -5, -3, -1, -4, -6, -7, -8, -9, -10]

bajoCero = 0

def temperaturaMinima(temperaturas):
    return min(temperaturas)

def temperaturaMaxima(temperaturas):
    return max(temperaturas)

def temperaturaPromedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)    

def temperaturasBajoCero(temperaturas):
    bajoCero = 0
    for temperatura in temperaturas:
        if temperatura < 0:
            bajoCero += 1
    return bajoCero

print("TEMPERATURAS DE JULIO (de menor a mayor)")
for temperatura in sorted(temperaturas):
    print(temperatura)
    
print("TEMPERATURAS")

print(f"MIN: {temperaturaMinima(temperaturas)}")
print(f"MAX: {temperaturaMaxima(temperaturas)}")
print(f"PROMEDIO: {temperaturaPromedio(temperaturas)}")
print(f"CANTIDAD DE DÍAS BAJO CERO: {temperaturasBajoCero(temperaturas)}")

