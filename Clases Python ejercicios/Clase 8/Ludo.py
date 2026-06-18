def pedirEntero():
    while True:
        try:
            tamaño = int(input("Ingrese el tamaño del tablero (entre 5 y 25): "))
            if 5 <= tamaño <= 25:
                return tamaño
            else:
                print("El tamaño debe estar entre 5 y 25. Intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def moverJugador(posicion, dado):
    return posicion + dado

jugador1 = ["Jugador 1"]
jugador2 = ["Jugador 2"]

tamañoTablero = pedirEntero()

posicionJugador1 = 0
posicionJugador2 = 0

import random

while True:
    dado1 = random.randint(1, 6)

    print(f"Jugador 1 obtuvo: {dado1}")

    posicionJugador1 = moverJugador(posicionJugador1, dado1)

    print(f"Jugador 1 se mueve a la posición {posicionJugador1}")

    if posicionJugador1 >= tamañoTablero:
        print("¡Jugador 1 gana!")
        break

    dado2 = random.randint(1, 6)

    print(f"Jugador 2 obtuvo: {dado2}")

    posicionJugador2 = moverJugador(posicionJugador2, dado2)

    print(f"Jugador 2 se mueve a la posición {posicionJugador2}")

    if posicionJugador2 >= tamañoTablero:
        print("¡Jugador 2 gana!")
        break

