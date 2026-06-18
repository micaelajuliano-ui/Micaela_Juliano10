precioBoleto = int(input("Ingrese el precio de cada boleto: "))
cantidadBoletos = int(input("Ingrese la cantidad de boletos que desea comprar: "))

if cantidadBoletos < 5:
    totalPagar = cantidadBoletos * precioBoleto
    print(f"El valor a pagar por {cantidadBoletos} entradas es de: ${totalPagar}")
else:
    print("Error. No se pudo realizar la venta. Cantidad máxima de entradas permitida: 4")


