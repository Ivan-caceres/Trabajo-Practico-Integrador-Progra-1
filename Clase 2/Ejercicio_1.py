# EJERCICIO 1
# Programa un sistema que pida al usuario ingresar una edad y luego clasifique a la persona según los siguientes rangos:
# 0 a 2 años → “Bebé”
# 3 a 12 años → “Niño”
# 13 a 17 años → “Adolescente”
# 18 a 64 años → “Adulto”
# 65 años o más → “Adulto mayor”

# Además:
# Si la edad ingresada es negativa o mayor a 120, el programa debe mostrar “Edad inválida”.

edad = int(input("Ingrese la edad a clasificar: "))

if edad >= 0 and edad <= 2:
    print("El sujeto es un bebé")
elif edad >= 3 and edad <= 12:
    print("El sujeto es un niño")
elif edad >= 13 and edad <= 17:
    print("El sujeto es un adolescente")
elif edad >= 18 and edad <= 64:
    print("El sujeto es un adulto")
elif edad < 0 or edad >= 120:
    print("Edad inválida")
else:
    print("El sujeto es un adulto mayor")