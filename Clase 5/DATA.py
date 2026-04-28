# Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
# Los datos requeridos son:
# Apellido
# Edad, entre 18 y 90 años inclusive.
# Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
# Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
# Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad (18 - 90): "))
estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ")
num_legajo = int(input("Ingrese su numero de legajo (1 - 9999): "))


while apellido == "":
    print("Ingrese nuevamente su apellido.")
    apellido = input("Ingrese su apellido: ")


while edad < 18 or edad > 90:
    print("Ingrese nuevamente su edad.")
    edad = int(input("Ingrese su edad (18 - 90): "))


while estado_civil != "Soltero/a" and estado_civil != "Casado/a" and estado_civil != "Divorciado/a" and estado_civil != "Viudo/a":
    print("Ingrese nuevamente su estado civil.")
    estado_civil = input("Ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a, Viudo/a): ")


while num_legajo < 1000 and num_legajo > 9999:
    print("Ingrese nuevamente su legajo.")
    num_legajo = int(input("Ingrese su numero de legajo (1 - 9999): "))


print(f"Su apellido es: {apellido}")
print(f"Su edad es: {edad} años")
print(f"Su estado civil es: {estado_civil}")
print(f"Su número de legajo es: {num_legajo}")