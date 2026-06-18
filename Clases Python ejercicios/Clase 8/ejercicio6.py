import random

lista = []
N = int(input("Ingrese la cantidad de números a generar: "))

while len(lista) < N:
    num = random.randint(0, 100)
    if num not in lista:
        lista.append(num)
print("Lista sin elementos repetidos (estrategia 1):", lista)

lista_con_repetidos = [random.randint(0, 100) for _ in range(N * 2)]  
lista_sin_repetidos = list(set(lista_con_repetidos))  

while len(lista_sin_repetidos) < N:  
    num = random.randint(0, 100)
    if num not in lista_sin_repetidos:
        lista_sin_repetidos.append(num)
print("Lista sin elementos repetidos (estrategia 2):", lista_sin_repetidos[:N])



