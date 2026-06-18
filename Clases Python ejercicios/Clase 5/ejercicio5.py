edadMayores = 0
edadMenores = 0

while True:
    edad = int(input("Ingrese una edad (entre 0 y 100, o -1 para finalizar): "))

    if edad == -1:
        break
    elif 0 < edad < 18:
        edadMenores += 1
    elif 18 <= edad <= 100:
        edadMayores += 1

sumaEdades = edadMayores + edadMenores
print(f"Hay {edadMenores} menores de edad")
print(f"Hay {edadMayores} mayores de edad")
print(f"La suma de ambas personas da {sumaEdades}")

