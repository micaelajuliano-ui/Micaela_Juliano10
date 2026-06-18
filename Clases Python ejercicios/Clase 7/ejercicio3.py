def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False

    numeros = sum(c.isdigit() for c in contraseña)
    mayusculas = sum(c.isupper() for c in contraseña)
    minusculas = sum(c.islower() for c in contraseña)

    if numeros < 2:
        return False
    if mayusculas < 1:
        return False
    if minusculas < 1:
        return False
    return True

contraseña_usuario = input("Ingrese una contraseña: ")
if validar_contraseña(contraseña_usuario):
    print("Contraseña válida.")
else:
    print("Contraseña inválida. Asegúrese de que tenga al menos 8 caracteres, 2 números, 1 mayúscula y 1 minúscula.")

