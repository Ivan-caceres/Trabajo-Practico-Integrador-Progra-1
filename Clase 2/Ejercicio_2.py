# EJERCICIO 2
# Sistema de verificación de acceso multinivel
# Implementar un programa que determine si un usuario puede acceder a una plataforma según tres factores:
# Rol del usuario: "admin", "editor", "viewer"
# Edad del usuario: número entero
# Clave de seguridad: un número entre 0 y 999
# El programa debe:
# Pedir los tres datos al usuario.
# Validar que la edad esté entre 0 y 120.
# Si no está en ese rango → "Edad inválida".
# Control de acceso según reglas:
# Si es admin:
# Tiene acceso total si la clave es 500 o mayor.
# Sino → "Clave insuficiente para admin".
# Si es editor:
# Debe tener 18 años o más y clave entre 100 y 499.
# Si no cumple → "Acceso denegado para editor".
# Si es viewer:
# Siempre tiene acceso si es mayor de 12 años, sin importar clave.
# Si es menor o igual a 12 → "Acceso denegado a menores".
# Si el rol ingresado no coincide con ninguno de los tres → "Rol inválido".

rol = input("Ingrese su rol: (admin/editor/viewer)")
edad = int(input("Ingrese su edad: "))
clave = int(input("Ingrese su clave: "))

match rol:
    case "admin":
        print("Su rol es administrador")
    case "editor":
        print("Su rol es editor")
    case "viewer":
        print("Su rol es viewer")
    case _:
        print("Rol inválido")
        exit()

if edad >= 0 and edad <= 120:
    print(f"Edad: {edad}")
else:
    print("Edad invalida")
    exit()

if rol == "admin":
    if clave >= 500:
        print("Usted tiene acceso total")
    else:
        print("Clave insuficiente para admin")

elif rol == "editor":
    if edad >= 18 and clave >= 100 and clave <= 499:
        print("Usted tiene acceso a servicios de editor")
    else:
        print("Acceso denegado para editor")

elif rol == "viewer":
    if edad > 12:
        print("Usted tiene acceso a servicios de observador")
    else:
        print("Acceso denegado a menores")

else:
    print("Rol inválido")