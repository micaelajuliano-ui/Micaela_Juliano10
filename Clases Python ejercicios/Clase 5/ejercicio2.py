tablaMultiplicar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

numero = int(input("Ingrese el número que desea multiplicar: "))
total = 0
for i in tablaMultiplicar:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    total += resultado
    

print(f"El resultado de la tabla de multiplicar es: {total}")

