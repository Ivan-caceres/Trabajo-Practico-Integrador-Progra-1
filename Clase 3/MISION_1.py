#Escena 1
print("=" * 50)
print("   GUARDIÁN GALÁCTICO - SISTEMA DE SEGURIDAD")
print("=" * 50)
print()

Nombre_jugador = input("¿Cuál es su nombre, cadete espacial? ")

print(f"Saludos, {Nombre_jugador}. El Guardián te pondrá a prueba...")

#Escena 2
print("=" * 50)
print("         PRUEBA 1: PRUEBA DE FUERZA")
print("=" * 50)

Numero_jugador_1 = int(input("Ingrese un número: "))

Numero_jugador_2 = int(input("Ingrese otro número: "))

print()

print(f"La sumatoria de los números ingresados es: {Numero_jugador_1 + Numero_jugador_2}")

print(f"La resta de los números ingresados es: {Numero_jugador_1 - Numero_jugador_2}")

print(f"El producto de los números ingresados es: {Numero_jugador_1 * Numero_jugador_2}")

print(f"El dividendo de los números ingresados es: {Numero_jugador_1 / Numero_jugador_2}")

print()

print("         ¡Prueba de fuerza superada!")

#Escena 3
print("=" * 50)
print("         PRUEBA 2: PRUEBA LÓGICA")
print("=" * 50)
print()

print(f"¿{Numero_jugador_1} es mayor que {Numero_jugador_2}? {Numero_jugador_1 > Numero_jugador_2}")

print(f"¿{Numero_jugador_1} es igual a {Numero_jugador_2}? {Numero_jugador_1 == Numero_jugador_2}")

print(f"¿{Numero_jugador_2} es menor o igual a 10? {Numero_jugador_2 <= 10}")

print()

#Escena 4
print("     ")

print("...Comienza la prueba final: la puerta de escape...")

if Numero_jugador_1 >= 0 and Numero_jugador_2 >= 0:
    print("Ambos números ingresados son positivos")

elif Numero_jugador_1 > 100 or Numero_jugador_2 > 100:
    print("Al menos uno de los números ingresados es mayor que 100")

elif Numero_jugador_1 != 0:
    print("El primer número ingresado no es cero")
