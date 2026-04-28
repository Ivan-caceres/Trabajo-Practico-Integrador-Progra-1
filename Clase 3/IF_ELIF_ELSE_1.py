# 1. 
# A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
# Menos de 160 cm: Base
# Entre 160 cm y 179 cm: Escolta
# Entre 180 cm y 199 cm: Alero
# 200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese su altura: "))

if altura >= 200:
    print("Su posicion es ala-pivot o pivot")
elif altura <= 199 and altura >= 180:
    print("Su posicion es alero")
elif altura <= 179 and altura >= 160:
    print("Su posicion es escolta")
elif altura <= 140:
    exit()
else:
    print("Su posicion es base")