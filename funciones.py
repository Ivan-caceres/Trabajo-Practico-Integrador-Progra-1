
def calcular_riesgo (estado_fw : str, porcentaje_carga_tt : int):
    """
    Calcula el nivel de riesgo del servidor
    estado_fw = Estado del firewall 
    porcentaje_carga_tt = El porcentaje total de carga 
    """
    if estado_fw == "Inactivo":
        nivel_estimado_riesgo += 5
    elif porcentaje_carga_tt > 80:
        nivel_estimado_riesgo += 3
    elif porcentaje_carga_tt > 95:
        nivel_estimado_riesgo += 2
    
    return nivel_estimado_riesgo

def calcular_estado_sv (nivel_riesgo : int):
    """
    Calcula el estado general del servidor
    nivel_riesgo = Es el nivel estimado de riesgo
    """

    if nivel_riesgo <= 3:
        estado_servidor = "Optimo"
    elif 3 < nivel_riesgo <= 6:
        estado_servidor = "Alerta"
    elif nivel_riesgo > 6:
        estado_servidor = "Critico"

    return estado_servidor

def calcular_carga(cpu : int, ram : int):
    """
    Calcular el estado de carga del servidor
    cpu = Uso de la cpu
    ram = Uso de la ram
    """
    if cpu >= 85 or ram >= 80:
        return "Sobrecarga critica"
    elif cpu > 70 or ram > 70:
        return "Carga elevada"
    elif cpu >= 40 or ram >= 40:
        return "Carga normal"
    else:
        return "Carga minima"
    
    
