cantidad1 = int(input("Ingrese la primer cantidad: "))
cantidad2 = int(input("Ingrese la segunda cantidad (distinta a la primera): "))
cantidad3 = int(input("Ingrese la tercera cantidad (distinta a las anteriores): "))

if cantidad1 > cantidad2 and cantidad1 > cantidad3:
    mayor = cantidad1
elif cantidad2 > cantidad1 and cantidad2 > cantidad3:
    mayor = cantidad2
else:
    mayor = cantidad3

print(f"La cantidad mayor es: {mayor}")