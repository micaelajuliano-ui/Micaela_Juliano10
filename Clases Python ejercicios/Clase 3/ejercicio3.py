tipoTarjeta = int(input("Ingrese su tipo de tarjeta: "))

if tipoTarjeta == 1:
    credito = 25
elif tipoTarjeta == 2:
    credito = 35
elif tipoTarjeta == 3:
    credito = 40
else:
    credito = 50

print(f"Según su tarjeta tipo {tipoTarjeta}, su nuevo límite de crédito es del {credito}%")




