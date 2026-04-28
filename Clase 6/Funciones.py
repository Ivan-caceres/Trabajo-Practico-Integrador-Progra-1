# 1. Crear una función que le solicite al usuario el ingreso de un número entero y lo retorne.

def ingresar_int() -> int:
    """
    Ingresa un numero entero y lo devuelve
    Arg:
        numero (int): Numero ingresado
    Return:
        int: Tipo de dato ingresado
    """
    num_int = int(input("Ingrese un numero: "))
    return num_int

print(ingresar_int())

# 2. Crear una función que le solicite al usuario el ingreso de un número flotante y lo retorne.

def ingresar_float() -> float:
    '''
    Ingresa un numero flotante y lo devuelve
    Arg:
        numero (float): Numero ingresado
    Return:
        float: Tipo de dato ingresado
    '''
    num_float = float(input("Ingrese un numero: "))
    return num_float

print(ingresar_float())

# 3. Crear una función que le solicite al usuario el ingreso de una cadena y la retorne. 

def ingresar_str() -> str:
    '''
    Ingresa una cadena de caracteres y la devuelve
    Arg:
        cadena (str) = Cadena de caracteres ingresada
    Return:
        str: Tipo de dato ingresado
    '''
    cadena = input("Ingrese una cadena de caracteres: ")
    return cadena

print(ingresar_str())

# 4. Escribir una función que calcule el área de un rectángulo. La función recibe la base y la altura y retorna el área.

def calculo_area_rectangulo() -> float:
    '''
    Ingrese base y altura, retorna area.
    Arg:
        base (float): Base ingresada en float
        altura (float): Altura ingresada en float
    Return:
        float: Tipo de dato del area calculada
    '''
    base = float(input("Ingrese la base del rectangulo: "))
    altura = float(input("Ingrese la altura del rectangulo: "))
    area = base * altura
    return area

print(calculo_area_rectangulo())

# 5. Escribe una función que calcule el área de un círculo. La función debe recibir el radio como parámetro y devolver el área.
# 6. Crea una función que verifique si un número dado es par o impar. La función debe imprimir un mensaje indicando si el número es par o impar.
# 7. Crea una función que verifique si un número dado es par o impar. La función retorna True si el número es par, False en caso contrario.
# 8. Define una función que encuentre el máximo de tres números. La función debe aceptar tres argumentos y devolver el número más grande.
# 9. Diseña una función que calcule la potencia de un número. La función debe recibir la base y el exponente como argumentos y devolver el resultado.
# 10. Crear una función que reciba un número y retorne True si el número es primo, False en caso contrario.
# 11. Crear una función que (utilizando el algoritmo del ejercicio de la guia de for), muestre todos los números primos comprendidos entre entre la unidad y un número ingresado como parámetro. La función retorna la cantidad de números primos encontrados. Modularizar todo lo posible.
# 12. Crear una función que imprima la tabla de multiplicar de un número recibido como parámetro. La función debe aceptar parámetros opcionales (inicio y fin) para definir el rango de multiplicación. Por defecto es del 1 al 10.
# 13. Especializar las funciones del punto 1, 2 y 3 para hacerlas reutilizables. Agregar validaciones.