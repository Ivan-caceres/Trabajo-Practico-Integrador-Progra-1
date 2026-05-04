from entrada_datos import *
from calculo_variables import *

def obtener_datos():
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

    return uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cant_procesos, so, firewall, tipo_serv, nombre_servidor, nombre_administrador

def evaluar_reglas(uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cant_procesos, so, firewall, 
                    tipo_serv, carga_total, recursos_disponibles, presion_por_proceso, ratio_usuarios, nivel_riesgo):


    if uso_cpu > 85 and uso_ram > 80 and carga_total > 82:
        alerta_critica = True
        mensaje_critica = f"CPU al {uso_cpu}%, RAM al {uso_ram}% y {cant_procesos} procesos activos superan los umbrales seguros."
    else:
        alerta_critica = False
        mensaje_critica = ""


    if espacio_libre < 10 or cant_procesos > 250:
        alerta_mantenimiento = True
        mensaje_mantenimiento = f"Espacio libre: {espacio_libre} GB. Procesos activos: {cant_procesos}."
    else:
        alerta_mantenimiento = False
        mensaje_mantenimiento = ""

    if not firewall == "Activo":
        alerta_seguridad = True
        mensaje_seguridad = f"Firewall en estado '{firewall}', servidor expuesto."
    else:
        alerta_seguridad = False
        mensaje_seguridad = ""

    if 40 <= uso_cpu <= 70 and 40 <= uso_ram <= 70:
        alerta_normal = True
        mensaje_normal = f"CPU al {uso_cpu}% y RAM al {uso_ram}% dentro de parámetros saludables."
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
        mensaje_proceso = f"Cada proceso consume en promedio {presion_por_proceso} unidades de carga."
    else:
        alerta_proceso = False
        mensaje_proceso = ""

    if recursos_disponibles < 20 and ratio_usuarios > 5 and nivel_riesgo in ("Alto", "Critico"):
        alerta_recursos = True
        mensaje_recursos = f"Solo {recursos_disponibles}% de recursos libres para {usuarios_conectados} usuarios."
    else:
        alerta_recursos = False
        mensaje_recursos = ""

    if so == "Windows Server" and espacio_libre < 20:
        alerta_disco = True
        mensaje_disco = f"Windows Server con solo {espacio_libre} GB libres. Mínimo recomendado: 20 GB."
    else:
        alerta_disco = False
        mensaje_disco = ""

    return (alerta_critica, alerta_mantenimiento, alerta_seguridad, alerta_normal, alerta_web, alerta_proceso, alerta_recursos, alerta_disco, mensaje_critica, mensaje_mantenimiento, mensaje_seguridad, mensaje_normal, mensaje_web, mensaje_proceso, mensaje_recursos, mensaje_disco)