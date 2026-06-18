autosPar = 0
autosImpar = 0
while True:
    patente = int(input("Ingrese la terminación de la patente (entre 0 y 9, o -1 para finalizar): "))
    if patente == -1:
        break
    elif 0 <= patente <= 9:
        if patente % 2 == 0:
            autosPar += 1
        else:
            autosImpar += 1
    else:
        print("Error. Por favor ingrese un número válido.")

print(f"Cantidad de vehículos con numeración par: {autosPar}")
print(f"Cantidad de vehículos con numeración impar: {autosImpar}")

