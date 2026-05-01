
def ingresar_uso_cpu() -> int:
    """Ingreso uso cpu y lo valida

    Returns:
        int: Valor ingresado
    """

    uso_cpu = int(input("Ingrese el uso de su CPU: "))

    while uso_cpu < 0 or uso_cpu > 100:
        uso_cpu = int(input("Error. Ingrese un valor entre 0 y 100: "))

    return uso_cpu

def ingresar_uso_ram() -> int:
    """Ingreso memoria RAM y la valida

    Returns:
        float: Valor ingresado
    """

    uso_ram = int(input("Ingrese memoria RAM (4,8,16,32,128): "))

    while uso_ram != 4 and uso_ram != 8 and uso_ram != 16 and uso_ram != 32 and uso_ram != 128:
        uso_ram = int(input("Error. Reingrese memoria RAM (4,8,16,32,128): "))

    return uso_ram

def ingresar_espacio_libre_disco() -> int:
    """Ingreso espacio libre en disco y lo valida

    Returns:
        float: Valor ingresado
    """

    espacio_libre_disco = int(input("Ingrese cuanto Espacio libre hay en el disco (GB): "))

    while espacio_libre_disco < 0 or espacio_libre_disco > 1000:
        espacio_libre_disco = int(input("Error. Ingrese un valor entre 0 y 1000: "))

    return espacio_libre_disco

def ingresar_usuarios_conectados() -> int:
    """Ingreso cantidad de usuarios conectados y la valida

    Returns:
        int: Valor ingresado
    """

    usuarios_conectados = int(input("Ingrese Cantidad de usuarios conectados: "))

    while usuarios_conectados < 0 or usuarios_conectados > 100:
        usuarios_conectados = int(input("Error. Reingrese un valor entre 0 y 100: "))

    return usuarios_conectados

def ingresar_cantidad_procesos_activos() -> int:
    """Ingreso cantidad de procesos activos y la valida

    Returns:
        int: Valor ingresado
    """

    cantidad_procesos_activos = int(input("Ingrese Cantidad de procesos activos: "))

    while cantidad_procesos_activos < 0 or cantidad_procesos_activos > 1000:
        cantidad_procesos_activos = int(input("Error. Ingrese cantidad de procesos activos entre 0 y 1000: "))

    return cantidad_procesos_activos

def ingresar_sistema_operativo() -> str:
    """Ingreso sistema operativo y lo valida

    Returns:
        str: Valor ingresado
    """

    sistema_operativo = input("Seleccione su sistema operativo Linux / Windows Server: ")

    while sistema_operativo != "Linux" and sistema_operativo != "Windows Server":
        sistema_operativo = input("Error. Seleccione Linux o Windows Server: ")

    return sistema_operativo
    
def ingresar_estado_firewall() -> str:
    """Ingreso estado del firewall y lo valida

    Returns:
        str: Valor ingresado
    """

    estado_firewall = input("Estado del firewall Activo / Inactivo: ")

    while estado_firewall != "Activo" and estado_firewall != "Inactivo":
        estado_firewall = input("Error. Reingrese Activo o Inactivo: ")

    return estado_firewall

def ingresar_tipo_servidor() -> str:
    """Ingreso tipo de servidor y lo valida

    Returns:
        str: Valor ingresado
    """

    tipo_servidor = input("Seleccione tipo de servidor Web / Base de datos / Archivos: ")

    while tipo_servidor != "Web" and tipo_servidor != "Base de datos" and tipo_servidor != "Archivos":
        tipo_servidor = input("Error. Reingrese Web / Base de datos / Archivos: ")

    return tipo_servidor

def ingresar_nombre_servidor() -> str:
    """Ingreso nombre del servidor y lo valida

    Returns:
        str: Valor ingresado
    """

    nombre_servidor = input("Ingrese nombre del servidor: ")

    while nombre_servidor.strip() == "":
        nombre_servidor = input("Error. Reingrese nombre del servidor: ")

    return nombre_servidor

def ingresar_nombre_administrador() -> str:
    """Ingreso nombre del administrador y lo valida

    Returns:
        str: Valor ingresado
    """

    nombre_administrador = input("Ingrese nombre del administrador responsable: ")

    while nombre_administrador.strip() == "":
        nombre_administrador = input("Error. Reingrese nombre del administrador responsable: ")

    return nombre_administrador


