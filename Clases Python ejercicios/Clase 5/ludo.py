contadorTiradas = 0
sumadorTiradas = 0

while sumadorTiradas < 24:
    valorDadoTirado = int(input("Ingrese el valor del dado (1 al 6): "))
    sumadorTiradas += valorDadoTirado
    contadorTiradas += 1
    
print("¡USTED HA GANADO!")