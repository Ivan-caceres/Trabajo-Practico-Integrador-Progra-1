from entrada_datos import *
from calculo_variables import *


def obtener_datos():
    """
    Reglas

    Invoca secuencialmente las funciones de ingreso del módulo "entrada_datos" y relaciona los valores ingresados con
    el mismo nombre de la variable obtenida en cada una de las funciones para utilizarla en condiciones posteriormente explicadas.

    Returns:
        tupla:
            - uso_cpu (int): Porcentaje de uso actual del CPU.

            - uso_ram (int): Porcentaje de uso actual de la memoria RAM.

            - espacio_libre (int): Espacio libre en disco expresado en gigabytes.

            - usuarios_conectados (int): Cantidad de usuarios conectados al servidor.

            - cant_procesos (int): Cantidad de procesos activos en el sistema.

            - so (str): Sistema operativo instalado en el servidor.

            - firewall (str): Estado actual del firewall del servidor.

            - tipo_serv (str): Tipo funcional del servidor.

            - nombre_servidor (str): Nombre identificador del servidor.

            - nombre_administrador (str): Nombre del administrador responsable.
    """
    uso_cpu = ingreso_uso_cpu()
    uso_ram = ingreso_uso_ram()
    espacio_libre = ingreso_espacio_libre()
    usuarios_conectados = ingreso_usuarios_conectados()
    cant_procesos = ingreso_cantidad_procesos()
    so = ingreso_so()
    firewall = ingreso_firewall()
    tipo_serv = ingreso_tipo_server()
    nombre_servidor = ingreso_nombre_server()
    nombre_administrador = ingreso_nombre_administrador()

    return (
        uso_cpu,
        uso_ram,
        espacio_libre,
        usuarios_conectados,
        cant_procesos,
        so,
        firewall,
        tipo_serv,
        nombre_servidor,
        nombre_administrador,
    )


def evaluar_reglas(
    uso_cpu,
    uso_ram,
    espacio_libre,
    usuarios_conectados,
    cant_procesos,
    so,
    firewall,
    tipo_serv,
    carga_total,
    recursos_disponibles,
    presion_por_proceso,
    ratio_usuarios,
    nivel_riesgo,
):
    """
    Evalúa el estado del servidor invocando las variables de los módulos entrada_datos y calculo_variables.

    Reglas predefinidas sobre los datos invocados, cada regla activa una bandera (bool) y construye un mensaje descriptivo cuando se cumple
    la condición asociada.

    Parametros:
        uso_cpu (int): Porcentaje de uso actual del CPU. (validado en entrada_datos)

        uso_ram (int): Porcentaje de uso actual de la memoria RAM. (validado en entrada_datos)

        espacio_libre (int): Espacio libre en disco expresado en gigabytes. (validado en entrada_datos)

        usuarios_conectados (int): Cantidad de usuarios conectados al servidor. (validado en entrada_datos)

        cant_procesos (int): Cantidad de procesos activos en el sistema. (validado en entrada_datos)

        so (str): Sistema operativo instalado en el servidor. (validado en entrada_datos)

        firewall (str): Estado actual del firewall del servidor. (validado en entrada_datos)

        tipo_serv (str): Tipo funcional del servidor. (validado en entrada_datos)

        carga_total (int): Promedio entre uso de CPU y RAM. (validado en calculo_variables)

        recursos_disponibles (int): Porcentaje de recursos libres del sistema. (validado en calculo_variables)

        presion_por_proceso (float): Carga promedio atribuida a cada proceso activo. (validado en calculo_variables)

        ratio_usuarios (float): Relación entre usuarios conectados y recursos disponibles. (validado en calculo_variables)

        nivel_riesgo (str): Nivel de riesgo clasificado por calculo_variables. (validado en calculo_variables)

    Returns:
        tupla:
            - alerta_critica (bool): True si CPU, RAM y carga total superan umbrales críticos.

            - alerta_mantenimiento (bool): True si el disco está casi lleno o hay exceso de procesos.

            - alerta_seguridad (bool): True si el firewall se encuentra inactivo.

            - alerta_normal (bool): True si CPU y RAM operan dentro de parámetros saludables.

            - alerta_web (bool): True si un servidor Web presenta alta carga con muchos usuarios.

            - alerta_proceso (bool): True si la presión por proceso supera el umbral aceptable.

            - alerta_recursos (bool): True si los recursos disponibles son insuficientes para la cantidad de usuarios conectados.

            - alerta_disco (bool): True si Windows Server opera con espacio en disco inferior al mínimo recomendado.

            - mensaje_critica (str): Descripción de la condición crítica detectada.

            - mensaje_mantenimiento (str): Descripción de la necesidad de mantenimiento.

            - mensaje_seguridad (str): Descripción del estado de seguridad del firewall.

            - mensaje_normal (str): Confirmación de operación dentro de parámetros normales.

            - mensaje_web (str): Descripción de la carga en el servidor Web.

            - mensaje_proceso (str): Descripción de la presión promedio por proceso.

            - mensaje_recursos (str): Descripción de la relación recursos/usuarios.

            - mensaje_disco (str): Descripción del estado del almacenamiento en disco.
    """

    if uso_cpu > 85 and uso_ram > 80 and carga_total > 82:
        alerta_critica = True
        mensaje_critica = f"CPU al {uso_cpu}%, RAM al {uso_ram}% y {cant_procesos} procesos activos superan los umbrales seguros."
    else:
        alerta_critica = False
        mensaje_critica = ""

    if espacio_libre < 10 or cant_procesos > 250:
        alerta_mantenimiento = True
        mensaje_mantenimiento = (
            f"Espacio libre: {espacio_libre} GB. Procesos activos: {cant_procesos}."
        )
    else:
        alerta_mantenimiento = False
        mensaje_mantenimiento = ""

    if firewall == "Inactivo":
        alerta_seguridad = True
        mensaje_seguridad = f"Firewall en estado '{firewall}', servidor expuesto."
    else:
        alerta_seguridad = False
        mensaje_seguridad = ""

    if 40 <= uso_cpu <= 70 and 40 <= uso_ram <= 70:
        alerta_normal = True
        mensaje_normal = (
            f"CPU al {uso_cpu}% y RAM al {uso_ram}% dentro de parámetros saludables."
        )
    else:
        alerta_normal = False
        mensaje_normal = ""

    if tipo_serv == "Web" and usuarios_conectados > 100 and uso_cpu > 75:
        alerta_web = True
        mensaje_web = f"{usuarios_conectados} usuarios conectados con CPU al {uso_cpu}% en servidor Web."
    else:
        alerta_web = False
        mensaje_web = ""

    if presion_por_proceso > 3 and (uso_cpu > 70 or uso_ram > 70):
        alerta_proceso = True
        mensaje_proceso = (
            f"Cada proceso consume en promedio {presion_por_proceso} unidades de carga."
        )
    else:
        alerta_proceso = False
        mensaje_proceso = ""

    if (
        recursos_disponibles < 20
        and ratio_usuarios > 5
        and nivel_riesgo in ("Alto", "Critico")
    ):
        alerta_recursos = True
        mensaje_recursos = f"Solo {recursos_disponibles}% de recursos libres para {usuarios_conectados} usuarios."
    else:
        alerta_recursos = False
        mensaje_recursos = ""

    if so == "Windows Server" or so == "windows server" and espacio_libre < 20:
        alerta_disco = True
        mensaje_disco = f"Windows Server con solo {espacio_libre} GB libres. Mínimo recomendado: 20 GB."
    else:
        alerta_disco = False
        mensaje_disco = ""

    return (
        alerta_critica,
        alerta_mantenimiento,
        alerta_seguridad,
        alerta_normal,
        alerta_web,
        alerta_proceso,
        alerta_recursos,
        alerta_disco,
        mensaje_critica,
        mensaje_mantenimiento,
        mensaje_seguridad,
        mensaje_normal,
        mensaje_web,
        mensaje_proceso,
        mensaje_recursos,
        mensaje_disco,
    )
