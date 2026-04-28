import Modulos_y_paquetes

opcion = int(input("Ingrese una opcion: "))
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if opcion == 1:
    print(Modulos_y_paquetes.sumar(num1=num1, num2=num2))
elif opcion == 2:
    print(Modulos_y_paquetes.restar(num1=num1, num2=num2))
elif opcion == 3:
    print(Modulos_y_paquetes.multiplicar(num1=num1, num2=num2))
elif opcion == 4:
    print(Modulos_y_paquetes.dividir(num1=num1, num2=num2))