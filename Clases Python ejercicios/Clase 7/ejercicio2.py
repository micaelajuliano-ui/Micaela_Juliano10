def esPanvocalica(palabra):
    vocales = "aeiouAEIOU"
    contadorVocales = 0

    for vocal in vocales:
        if vocal in palabra:
            contadorVocales += 1

    return contadorVocales == 5

palabra1 = "centrifugado"
palabra2 = "casa"

print(f"{palabra1} es panvocálica: {esPanvocalica(palabra1)}")
print(f"{palabra2} es panvocálica: {esPanvocalica(palabra2)}")




