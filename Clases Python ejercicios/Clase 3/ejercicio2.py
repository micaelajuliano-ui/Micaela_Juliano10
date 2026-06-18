precioProducto = int(input("Ingrese el precio del producto: "))
montoAbonado = int(input("Ingrese el monto abonado: "))

if montoAbonado >= precioProducto:
    vuelto = montoAbonado - precioProducto
    print(f"El vuelto de su compra es: ${vuelto}")
else:
    print("Dinero insuficiente")


