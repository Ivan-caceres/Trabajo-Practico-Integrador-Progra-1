def ingreso_uso_cpu() -> int:
    """
    Ingresa el porcentaje de uso actual del CPU.

    Valida que el valor ingresado esté entre 0 y 100, en caso contrario reingresa el porcentaje con esas condiciones.

    Returns:
        int: Porcentaje de uso del CPU, entre 0 y 100.
    """

    uso_cpu = int(input("Ingrese el uso actual de su CPU (%): "))

    while uso_cpu < 0 or uso_cpu > 100:
        uso_cpu = int(input("Ingrese un valor entre 0 y 100: "))

    return uso_cpu


def ingreso_uso_ram() -> int:
    """
    Ingresa el porcentaje de uso actual de la memoria RAM.

    Valida que el valor ingresado esté entre 0 y 100, en caso contrario reingresar el porcentaje con esas condiciones.

    Returns:
        int: Porcentaje de uso de la RAM, entre 0 y 100.
    """

    uso_ram = int(input("Ingrese el uso actual de su RAM (%): "))

    while uso_ram < 0 or uso_ram > 100:
        uso_ram = int(input("Ingrese un valor entre 0 y 100: "))

    return uso_ram


def ingreso_espacio_libre() -> int:
    """
    Ingresa el espacio libre actual de su sistema en GB.

    Valida que el valor ingresado no sea negativo, en caso contrario reingresar el valor expresado en GB.

    Returns:
        int: Espacio libre en disco expresado en GB, mayor que 0.
    """
    espacio_libre = int(input("Ingrese el espacio libre en disco (GB): "))

    while espacio_libre < 0:
        espacio_libre = int(
            input(
                "No se admite la ejecucion del ingreso si no tiene espacio libre en el sitema. Vuelva a intentarlo: "
            )
        )

    return espacio_libre


def ingreso_usuarios_conectados() -> int:
    """
    Ingresa la cantidad de usuarios conectados al servidor.

    Valida que el valor ingresado sea mayor que 0, en caso contrario reingresar la cantidad de usuarios conectados.

    Returns:
        int: Cantidad de usuarios conectados al servidor, mayor que 0.
    """
    usuarios_conectados = int(input("Ingrese la cantidad de usuarios conectados: "))

    while usuarios_conectados <= 0:
        usuarios_conectados = int(input("Ingrese una cantidad de usuarios valida: "))

    return usuarios_conectados


def ingreso_cantidad_procesos() -> int:
    """
    Ingresa la cantidad de procesos activos actualmente en el servidor.

    Valida que el ingreso de procesos sea mayor a 0, en caso contrario reingresar la cantidad de procesos actuales.

    Returns:
        int: Cantidad de procesos activos, mayor a cero.
    """
    cantidad_procesos = int(input("Ingrese la cantidad de procesos activos: "))

    while cantidad_procesos <= 0:
        cantidad_procesos = int(input("Ingrese una cantidad de procesos valida: "))

    return cantidad_procesos


def ingreso_so() -> str:
    """
    Ingresa el sistema operativo instalado en el servidor.

    Valida que se ingrese una de las opciones predefinidas ["Linux" o "Windows Server"], no discrimina si se ingresó sin mayúsculas. En caso contrario reingresar un SO válido.

    Returns:
        str: Sistema operativo del servidor. Opciones disponibles: "Linux", "Windows Server", "linux", "windows server".
    """
    so = input("Ingrese su sistema operativo(Linux / Windows Server): ")

    while (
        so != "Linux"
        and so != "Windows Server"
        and so != "linux"
        and so != "windows server"
    ):
        so = input("Ingrese un sistema operativo valido(Linux / Windows Server): ")

    return so


def ingreso_firewall() -> str:
    """
    Ingresa el estado actual del Firewall del servidor.

    Valida que se ingrese una de las opciones predefinidas ["Activo" o "Inactivo"], no discrimina si se ingresó sin mayúsculas. En caso contrario reingresar una opción válida.

    Returns:
        str: Estado actual del firewall del servidor. Opciones disponibles: "Activo", "Inactivo", "activo", "inactivo".
    """
    firewall = input("Ingrese el estado del Firewall(Activo / Inactivo): ")

    while (
        firewall != "Activo"
        and firewall != "Inactivo"
        and firewall != "activo"
        and firewall != "inactivo"
    ):
        firewall = input("Ingrese un estado valido(Activo / Inactivo): ")

    return firewall


def ingreso_tipo_server() -> str:
    """
    Ingresa el tipo de servidor a diagnosticar.

    Valida que se ingrese una de las opciones predefinidas ["Web" o "Base de datos" o "Archivos"], no discrimina si se ingresó sin mayúsculas. En caso contrario reingresar un tipo de servidor válido.

    Returns:
        str: Tipo de servidor a diagnosticar. Opciones disponibles: "Web", "Base de datos", "Archivos", "web", "base de datos", "archivos".
    """
    tipo_serv = input("Ingrese el tipo de servidor(Web / Base de datos / Archivos): ")

    while (
        tipo_serv != "Web"
        and tipo_serv != "Base de datos"
        and tipo_serv != "Archivos"
        and tipo_serv != "web"
        and tipo_serv != "base de datos"
        and tipo_serv != "archivos"
    ):
        tipo_serv = input(
            "Ingrese un tipo de servidor valido(Web / Base de datos / Archivos): "
        )

    return tipo_serv


def ingreso_nombre_server() -> str:
    """
    Ingresa el nombre del servidor a diagnosticar.

    Valida que la cadena ingresada no esté vacía o compuesta de espacios en blanco. En caso contrario reingresar nombre del servidor a diagnosticar.

    Returns:
        str: Nombre del servidor a diagnosticar, asegura que no esté vacío o compuesto por espacios en blanco.
    """
    nombre_servidor = input("Ingrese el nombre del servidor: ")

    while nombre_servidor.strip() == "":
        nombre_servidor = input("Ingrese el nombre del servidor: ")

    return nombre_servidor


def ingreso_nombre_administrador() -> str:
    """
    Ingresa el nombre del administrador responsable del servidor a diagnosticar.

    Valida que la cadena ingresada no esté vacía o compuesta de espacios en blanco. En caso contrario reingresar nombre del administrador responsable.

    Returns:
        str: Nombre de usuario del administrador, asegura que no esté vacío o compuesto por espacios en blanco.
    """
    nombre_administrador = input("Ingrese su nombre de usuario: ")

    while nombre_administrador.strip() == "":
        nombre_administrador = input("Ingrese su nombre de usuario: ")
    return nombre_administrador
