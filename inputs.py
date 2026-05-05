'''
Categóricos (3 mínimo). Opciones cerradas. Ejemplos: 
Sistema operativo (Linux / Windows Server) 
Estado del firewall (Activo / Inactivo) 
Tipo de servidor (Web / Base de datos / Archivos) 
Cadenas (2 mínimo) Ejemplos: Nombre del servidor / Nombre del administrador responsable 
10 INPUTS: Numéricos 5, Categóricos 3 y Cadenas 2 
VALIDACIONES de ingreso: solo números, coincidencia de opciones  y mínimo un espacio ¿?
'''
#validar con un while el ingreso de los 10 dtos, si responde una, pasa a la otra 
#validar que se ingresen numeros


def ingreso_uso_cpu() -> int:
    """
    Ingresa el uso actual del CPU y lo valida.
    """

    uso_cpu = int(input("Ingrese el uso actual de su CPU (%): "))

    while uso_cpu < 0 or uso_cpu > 100:
        uso_cpu = int(input("Ingrese un valor entre 0 y 100: "))
    
    return uso_cpu

def ingreso_uso_ram() -> int:
    """
    Ingresa el uso actual de la memoria RAM y lo valida. 
    """

    uso_ram = int(input("Ingrese el uso actual de su RAM (%): "))

    while uso_ram < 0 or uso_ram > 100:
        uso_ram = int(input("Ingrese un valor entre 0 y 100: "))
    
    return uso_ram

def ingreso_espacio_libre() -> int:
    """
    Ingresa el espacio libre actual de su sistema.
    """
    espacio_libre = int(input("Ingrese el espacio libre en disco (GB): "))

    while espacio_libre < 0:
        espacio_libre = int(input("No se admite la ejecucion del ingreso si no tiene espacio libre en el sitema. Vuelva a intentarlo: "))

    return espacio_libre

def ingreso_usuarios_conectados() -> int:
    """
    Ingresa la cantidad de usuarios conectados.
    """
    usuarios_conectados = int(input("Ingrese la cantidad de usuarios conectados: "))

    while usuarios_conectados <= 0:
        usuarios_conectados = int(input("Ingrese una cantidad de usuarios valida: "))
    
    return usuarios_conectados

def ingreso_cantidad_procesos() -> int:
    """
    Ingresa la cantidad de procesos activos.
    """
    cantidad_procesos = int(input("Ingrese la cantidad de procesos activos: "))

    while cantidad_procesos <= 0:
        cantidad_procesos = int(input("Ingrese una cantidad de procesos valida: "))
    
    return cantidad_procesos

def ingreso_so() -> str:
    """
    Ingresa el sistema operativo y lo valida.
    """
    so = input("Ingrese su sistema operativo(Linux / Windows Server): ")
    
    while so != "Linux" and so != "Windows Server" and so != "linux" and so != "windows server":
        so = input("Ingrese un sistema operativo valido(Linux / Windows Server): ")
    
    return so

def ingreso_firewall() -> str:
    """
    Ingresa el estado del Firewall y lo valida.
    """
    firewall = input("Ingrese el estado del Firewall(Activo / Inactivo): ")

    while firewall != "Activo" and firewall != "Inactivo" and firewall != "activo" and firewall != "inactivo":
        firewall = input("Ingrese un estado valido(Activo / Inactivo): ")

    return firewall

def ingreso_tipo_server() -> str:
    """
    Ingresa el tipo de servidor y lo valida.
    """
    tipo_serv = input("Ingrese el tipo de servidor(Web / Base de datos / Archivos): ")
    
    while tipo_serv != "Web" and tipo_serv != "Base de datos" and tipo_serv != "Archivos" and tipo_serv != "web" and tipo_serv != "base de datos" and tipo_serv != "archivos":
        tipo_serv = input("Ingrese un tipo de servidor valido(Web / Base de datos / Archivos): ")

    return tipo_serv

def ingreso_nombre_server() -> str:
    """
    Ingresa el nombre del servidor y lo valida.
    """
    nombre_servidor = input("Ingrese el nombre del servidor: ")

    while nombre_servidor.strip() == "":
        nombre_servidor = input("Ingrese el nombre del servidor: ")

    return nombre_servidor

def ingreso_nombre_administrador() -> str:
    """
    Ingresa el nombre del administrador responsable y lo valida.
    """
    nombre_administrador = input("Ingrese su nombre de usuario: ")

    while nombre_administrador.strip() == "":
        nombre_administrador = input("Ingrese su nombre de usuario: ")
    return nombre_administrador