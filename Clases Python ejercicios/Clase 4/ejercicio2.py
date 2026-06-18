print("Ingrese los precios de los productos comprados. Ingrese 0 para finalizar.")

precioFinal = 0
cantidadProductos = 0

while True:
    precio = int(input("Ingrese el precio del producto: "))

    if precio == 0:
        break

    precioFinal += precio
    cantidadProductos += 1

print(f"El total de la compra es: {precioFinal}")
print(f"La cantidad de productos es: {cantidadProductos}")









