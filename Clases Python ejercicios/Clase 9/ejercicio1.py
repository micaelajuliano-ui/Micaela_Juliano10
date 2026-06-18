def guardar_nombres():
    with open("alumnos.txt", "w") as archivo:
        for i in range(5):
            nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
            archivo.write(nombre + "\n")

def leer_nombres():
    with open("alumnos.txt", "r") as archivo:
        nombres = archivo.readlines()
        return [nombre.strip() for nombre in nombres]
    
def mostrar_nombres(nombres):
    for index, nombre in enumerate(nombres, start=1):
        print(f"{index} - {nombre}")

def contar_alumnos(nombres):
    return len(nombres)

guardar_nombres()
nombres = leer_nombres()    
mostrar_nombres(nombres)
cantidad_alumnos = contar_alumnos(nombres)
print(f"Total de alumnos: {cantidad_alumnos}")