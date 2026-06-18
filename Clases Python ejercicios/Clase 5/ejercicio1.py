lista = []
n = 1
numeros = 0

while numeros != -1:
    numeros = int(input(f"Ingrese el {n} número: ")) 
    n += 1
    lista.append(numeros)


lista.remove(-1)
print(f"El mayor número de la lista es: {max(lista)}")
print(f"El menor número de la lista es: {min(lista)}")




