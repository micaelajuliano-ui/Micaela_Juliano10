def contar_palabra_python():
    with open("texto.txt", "r") as archivo:
        lineas = archivo.readlines()
        contador = 0
        for linea in lineas:
            contador += linea.lower().count("python")
        return contador
total_python = contar_palabra_python()
print(f"La palabra python aparece {total_python} veces")
