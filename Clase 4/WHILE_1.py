#5. Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.

# contador = 0
# suma = 0

# while contador < 5:
#     numero = int(input(f"Ingrese un número: "))
#     suma += numero
#     contador += 1

# print(f"El contador termina en: {contador}")
# print(f"La suma de los numeros ingresados es: {suma}")
# print(f"El promedio de los numeros ingresados es: {suma / contador}")

#6. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0
# continuar = "s"

# while continuar == "s":
#     numero = int(input("Ingrese un numero: "))
#     contador += 1
#     suma += numero
#     continuar = input("¿Desea continuar ingresando números? (s/n): ")

# print(f"La suma de los numeros ingresados es {suma}")
# print(f"El promedio de los numeros ingresados es {suma / contador}")

#7. Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

# suma = 0
# producto = 1
# continuar = "s"

# while continuar == "s":
#     numero = int(input("Ingrese un numero: "))
#     if numero > 0:
#         suma += numero
#     else:
#         producto *= numero
#     continuar = input("¿Desea continuar ingresando números? (s/n): ")

# print(f"La suma de los numeros ingresados es {suma}")
# print(f"El producto de los numeros negativos ingresados es {producto}")

#8. Ingresar 10 números enteros. Determinar el máximo y el mínimo.

# cantidad = 10
# minimo = float('inf')
# maximo = float('-inf')

# for i in range(1, cantidad):
#     numero = int(input(f"Ingrese un numero {i}: "))
#     if numero > maximo:
#         maximo = numero
#     elif numero < minimo:
#         minimo = numero

# print(f"El numero maximo ingresado fue {maximo}")
# print(f"El numero minimo ingresado fue {minimo}")

#9. Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0

# while True:
#     numero = int(input(f"Ingrese un numero {contador + 1}: "))
#     suma += numero
#     contador += 1

#     continuar = input("¿Desea continuar ingresando números? (s/n): ")

#     if continuar == "n":
#         print(f"Debe ingresar al menos 5 números. Lleva {contador}.")
#     else:
#         break

# print(f"Se ingresaron {contador} numeros")
# print(f"La suma de los numeros ingresados es {suma}")
# print(f"El promedio de los numeros ingresados es {suma / contador}")

#10. Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

# contador = 0
# suma = 0
# continuar = "s"

# while contador <= 10:
#     numero = int(input(f"Ingrese un numero {contador + 1}: "))
#     suma += numero
#     contador += 1

#     if contador == 10:
#         print("Llegaste al numero maximo de ingresos")
#         break

#     continuar = input("¿Desea continuar ingresando números? (s/n): ")

#     if continuar == "n":
#         if contador < 5:
#             print(f"Debe ingresar al menos 5 números. Lleva {contador}.")
#             continuar = "s"
#         else:
#             break

# print(f"Se ingresaron {contador} numeros")
# print(f"La suma de los numeros ingresados es {suma}")
# print(f"El promedio de los numeros ingresados es {suma / contador}")