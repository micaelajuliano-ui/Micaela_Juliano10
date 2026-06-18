import time
time.sleep(1)

hora = int(input("Ingrese la hora (0 a 24): "))
minuto = int(input("Ingrese el minuto (0 a 60): "))
segundo = int(input("Ingrese el segundo (0 a 60): "))

while hora != 0 or minuto != 0 or segundo != 0:
    print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
    
    segundo -= 1
    
    if segundo < 0:
        segundo = 59
        minuto -= 1
        
    if minuto < 0:
        minuto = 59
        hora -= 1
        
    if hora < 0:
        hora = 23
print("<<<< TIEMPO >>>>")



