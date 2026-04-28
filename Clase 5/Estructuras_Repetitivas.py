nombre_empleado = input("Ingrese el nombre del empleado: ")
edad_empleado = int(input("Ingrese la edad del empleado (18 - 65): "))
genero_empleado = input("Ingrese el género del empleado (M/F/O): ")
tecnologia_elegida = input("Ingrese la tecnología elegida (IA, RV/RA, IOT): ")


while edad_empleado < 18 or edad_empleado > 65:
        print("Ingreso incorrecto, vuelva a intentarlo")
        edad_empleado = int(input("Ingrese la edad del empleado (18 - 65): "))


while genero_empleado != "M" and genero_empleado != "F" and genero_empleado != "O":
        print("Ingreso incorrecto, vuelva a intentarlo")
        genero_empleado = input("Ingrese el género del empleado (M/F/O): ")


while tecnologia_elegida != "IA" and tecnologia_elegida != "RV/RA" and tecnologia_elegida != "IOT":
        print("Ingreso incorrecto, vuelva a intentarlo")
        tecnologia_elegida = input("Ingrese la tecnología elegida (IA, RV/RA, IOT): ")


edad_max = float("-inf")
nombre_mayor = ""
tecnologia_mayor = ""

contador_empleados = 0
iot_ia_masc_25_50 = 0
not_ia_notfem_33_40 = 0


while contador_empleados < 10: #Bucle general
    print(f"Empleado {contador_empleados + 1}:")
    print(f"Nombre: {nombre_empleado}")
    print(f"Edad: {edad_empleado}")
    print(f"Género: {genero_empleado}")
    print(f"Tecnología Elegida: {tecnologia_elegida}")
    print("-----------------------------")

    nombre_empleado = input("Ingrese el nombre del empleado: ")
    edad_empleado = int(input("Ingrese la edad del empleado: (18 - 65)"))
    genero_empleado = input("Ingrese el género del empleado (M/F/O): ")
    tecnologia_elegida = input("Ingrese la tecnología elegida (IA, RV/RA, IOT): ")

    if edad_empleado > edad_max:
        edad_max = edad_empleado
        nombre_mayor = nombre_empleado
        tecnologia_mayor = tecnologia_elegida

    if genero_empleado == "M": #Condicion punto 3
        print(f"El empleado mayor: {nombre_mayor} voto {tecnologia_mayor} y tiene {edad_max}")


    while iot_ia_masc_25_50 < 10: #Bucle punto 1
        if genero_empleado == "M" and (tecnologia_elegida == "IA" or tecnologia_elegida == "IOT") and edad_empleado >= 25 and edad_empleado <= 50:
            iot_ia_masc_25_50 += 1


    while not_ia_notfem_33_40 < 10: #Bucle punto 2
        if tecnologia_elegida != "IA" and genero_empleado != "F" and edad_empleado >= 33 and edad_empleado <= 40:
            not_ia_notfem_33_40 += 1

        contador_empleados += 1


print(f"Cantidad de empleados masculinos entre 25 y 50 años que eligieron IA o IOT: {iot_ia_masc_25_50}")
print(f"Porcentaje de empleados que no eligieron IA, no son mujeres y tienen entre 33 y 40 años: {not_ia_notfem_33_40 / contador_empleados * 100:.2f}%")