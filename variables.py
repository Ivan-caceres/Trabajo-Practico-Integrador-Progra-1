from funciones import (calcular_riesgo, calcular_estado_sv, calcular_carga)
from inputs import(uso_cpu, uso_ram, espacio_libre_disco, cantidad_procesos_activos, estado_firewall)


porcentaje_total_carga =  (uso_cpu + uso_ram) / 2

nivel_estimado_riesgo = calcular_riesgo(estado_firewall, porcentaje_total_carga)

ram_disponible_porcentaje = 100 - uso_ram
recursos_disponibles = f"Disco: {espacio_libre_disco}GB \nRam libre: {ram_disponible_porcentaje}%"

estado_general_servidor = calcular_estado_sv(nivel_estimado_riesgo)

estado_carga = calcular_carga(uso_cpu, uso_ram)