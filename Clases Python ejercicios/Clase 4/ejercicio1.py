precioProducto = int(input("Ingrese el precio del producto (0 para terminar): "))

while precioProducto != 0:
    montoAbonado = int(input("Ingrese el monto abonado: "))
    
    if montoAbonado >= precioProducto:
        vuelto = montoAbonado - precioProducto
        print(f"El vuelto de su compra es: ${vuelto}")
    else:
        print("Dinero insuficiente")
    
    precioProducto = int(input("Ingrese el precio de otro producto (0 para terminar): "))

print("¡Gracias por su compra!")





