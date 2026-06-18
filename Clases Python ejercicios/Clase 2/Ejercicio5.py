salarioMensual = int(input("Ingrese su salario mensual: "))
porcentajeAhorro = int(input("Ingrese su porcentaje de ahorro: "))
precioProducto = int(input("Ingrese el valor del producto que desea comprar: "))

ahorroMensual = salarioMensual * (porcentajeAhorro / 100)

meses = 1
ahorro = ahorroMensual

while ahorro < precioProducto:
    ahorro += ahorroMensual
    meses += 1
    
print(f"Para comprar el producto deseado hacen falta {meses} meses")





