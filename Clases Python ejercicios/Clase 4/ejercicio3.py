

while True:
    cantidadAlumnos = int(input("Ingrese la cantidad de alumnos que rindieron el examen: "))

    if cantidadAlumnos == 0:
        break

    sumaNotas = 0

    for i in range(cantidadAlumnos):
        nota = float(input(f"Ingrese la nota del alumno {i + 1}: "))
        sumaNotas += nota

    promedio = sumaNotas / cantidadAlumnos
    print(f"La nota promedio del curso es: {promedio}")

