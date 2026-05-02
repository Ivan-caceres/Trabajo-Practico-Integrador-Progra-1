def calculo_variables(uso_cpu, uso_ram, espacio_libre, usuarios_conec, cant_proc, tipo_serv):

    carga_total = (uso_cpu + uso_ram) / 2

    recursos_disponibles = 100 - carga_total

    uso_por_proc = ((uso_cpu + uso_ram / cant_proc, 2)) if cant_proc > 0 else 0

    ratio_user = (usuarios_conec / recursos_disponibles, 2) if recursos_disponibles > 0 else float('inf')

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
        estado_general == "Estado del sistema en leve estres"
    else:
        estado_general == "Estado del sistema normal"
    
    return carga_total, recursos_disponibles, uso_por_proc, ratio_user, nivel_riesgo, estado_general
