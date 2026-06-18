factorial = 1
while True:
    numero = int(input("Ingrese un número entero mayor que cero para calcular su factorial (o -1 para finalizar): "))
    if numero == -1:
        break
    elif numero > 0:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        print(f"El factorial de {numero} es: {factorial}")
    else:
        print("Error. Por favor ingrese un número válido")



