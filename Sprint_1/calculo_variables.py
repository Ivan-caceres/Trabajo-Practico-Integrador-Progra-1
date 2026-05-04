from entrada_datos import *

def calculo_variables(uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cantidad_procesos, tipo_serv):

    carga_total = (uso_cpu + uso_ram) / 2

    recursos_disponibles = 100 - carga_total

    uso_por_proc = (uso_cpu + uso_ram) / cantidad_procesos

    ratio_usuario = usuarios_conectados / recursos_disponibles


    if cantidad_procesos > 0:
        uso_por_proc = (uso_cpu + uso_ram) / cantidad_procesos
    else:
        uso_por_proc = 0

    if recursos_disponibles > 0:
        ratio_usuario = usuarios_conectados / recursos_disponibles
    else:
        ratio_usuario = float('inf')

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
    
    return carga_total, recursos_disponibles, uso_por_proc, ratio_usuario, nivel_riesgo, estado_general