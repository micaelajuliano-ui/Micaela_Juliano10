import time
time.sleep(1)

hora = int(input("Ingrese la hora (0 a 24): "))
minuto = int(input("Ingrese el minuto (0 a 60): "))
segundo = int(input("Ingrese el segundo (0 a 60): "))

while True:
    print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")
    
    segundo += 1
    
    if segundo > 59:
        segundo = 0
        minuto += 1
        
    if minuto > 59:
        minuto = 0
        hora += 1
        
    if hora > 23:
        hora = 0





