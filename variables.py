from inputs import *


def calculo_variables(
    uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cantidad_procesos, _
):
    """
    Motor de diagnóstico de riesgo

    En base a las variables obtenidas del módulo "entrada_datos"(uso de cpu, ram, espacio libre en disco y cantidad de usuarios/procesos),
    se calcula promiedos que cuantifican la carga del sistema, los recursos disponibles en el mismo, el uso promedio de estos recursos
    en base a cada proceso y la relación entre usuarios conectados y los recursos disponibles.

    Args:
        uso_cpu (int): Porcentaje de uso del CPU, entre 0 y 100.

        uso_ram (int): Porcentaje de uso de la memoria RAM, entre 0 y 100.

        espacio_libre (int): Espacio libre en disco expresado en GB, mayor que 0.

        usuarios_conectados (int): Cantidad de usuarios conectados, mayor que 0.

        cantidad_procesos (int): Cantidad de procesos activos actualmente en el sistema, mayor que 0.

    Returns:
        tupla:
            - carga_total (int): Promedio de uso entre CPU y RAM. Carga total del sistema.

            - recursos_disponibles (int): Porcentaje de recursos sin utilizar. Complemento de la carga_total.

            - uso_por_proceso (int): Carga promedio por proceso activo. Cociente de la sumatoria entre uso del CPU y ram, y
            la cantidad de procesos activos

            - ratio_usuario (float): Relación entre los usuarios conectados y los recursos disponibles. Retorna inf(indeterminado) si los
            recursos disponibles son cero.

            - nivel_riesgo (str): Clasificación de riesgo del sistema, de forma descendente "Critico", "Alto", "Medio, "Bajo".

            - estado_general (str): Descripción del estado actual del servidor dependiendo del nivel de riesgo que devolvió.
    """

    carga_total = (uso_cpu + uso_ram) / 2

    recursos_disponibles = 100 - carga_total

    uso_por_proceso = (uso_cpu + uso_ram) / cantidad_procesos

    ratio_usuario = usuarios_conectados / recursos_disponibles

    if cantidad_procesos > 0:
        uso_por_proceso = (uso_cpu + uso_ram) / cantidad_procesos
    else:
        uso_por_proceso = 0

    if recursos_disponibles > 0:
        ratio_usuario = usuarios_conectados / recursos_disponibles

    if carga_total > 85 or espacio_libre < 5:
        nivel_riesgo = "Critico"
    elif carga_total > 65 or espacio_libre < 15:
        nivel_riesgo = "Alto"
    elif carga_total > 40:
        nivel_riesgo = "Medio"
    else:
        nivel_riesgo = "Bajo"

    if nivel_riesgo == "Critico":
        estado_general = "Estado del sistema en peligro"
    elif nivel_riesgo == "Alto":
        estado_general = "Estado del sistema en grave estres"
    elif nivel_riesgo == "Medio":
        estado_general = "Estado del sistema en leve estres"
    else:
        estado_general = "Estado del sistema normal"

    return (
        carga_total,
        recursos_disponibles,
        uso_por_proceso,
        ratio_usuario,
        nivel_riesgo,
        estado_general,
    )
