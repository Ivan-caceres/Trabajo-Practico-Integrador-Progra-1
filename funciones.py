
"""def app():
    print("***"*22)
    print("Bienvenido al Sistema de Diagnostico y Configuracion del Servidor")
    print("***"*22)
    cpu_uso = ingresar_uso_cpu()
    ram_uso = ingresar_uso_ram()
    espacio_libre_gb = ingreso_espacio_libre_disco()
    usuarios_online = ingresos_datos
"""

def calcular_riesgo (estado_fw : str, porcentaje_carga_tt : int) -> int:
    """
    Calcula el nivel de riesgo del servidor
    Args:
        estado_fw (str) = Estado del firewall 
        porcentaje_carga_tt (int) = El porcentaje total de carga
    Return:
        int: Valor numerico representando el nivel de riesgo del servidor
    """
    if estado_fw == "Inactivo":
        nivel_estimado_riesgo += 5
    elif porcentaje_carga_tt > 80:
        nivel_estimado_riesgo += 3
    elif porcentaje_carga_tt > 95:
        nivel_estimado_riesgo += 2
    
    return nivel_estimado_riesgo

def calcular_estado_sv (nivel_riesgo : int) -> str:
    """
    Calcula el estado general del servidor
    Args:
        nivel_riesgo = Es el nivel estimado de riesgo
    return:

    """

    if nivel_riesgo <= 3:
        estado_servidor = "Optimo"
    elif 3 < nivel_riesgo <= 6:
        estado_servidor = "Alerta"
    elif nivel_riesgo > 6:
        estado_servidor = "Critico"

    return estado_servidor

def calcular_carga(cpu : int, ram : int) -> str:
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
    
def estado_disco(disco_libre : int, procesos : int) -> str:
    pass
