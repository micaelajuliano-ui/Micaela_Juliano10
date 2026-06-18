valorArticulo = int(input("Ingrese el valor del artículo: "))

descuento = valorArticulo * 0.2
valorConDescuento = valorArticulo - descuento

iva = valorConDescuento * 0.21
valorConIva = valorConDescuento + iva

print(f"El valor del artículo con el descuento es de ${valorConDescuento}")
print(f"El valor final del artículo es de: ${valorConIva}")


