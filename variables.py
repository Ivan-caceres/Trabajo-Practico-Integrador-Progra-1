from funciones import (calcular_riesgo, calcular_estado_sv)

uso_cpu = 50 #esto conecta con los input
uso_ram = 60 #esto conecta con los input
espacio_libre_gb = 200 #esto conecta con los input
estado_firewall = "Activo" #esto conecta con los input


porcentaje_total_carga =  (uso_cpu + uso_ram) / 2

nivel_estimado_riesgo = calcular_riesgo(estado_firewall, porcentaje_total_carga)

ram_disponible_porcentaje = 100 - uso_ram
recursos_disponibles = f"Disco: {espacio_libre_gb}GB \nRam libre: {ram_disponible_porcentaje}%"

estado_general_servidor = calcular_estado_sv(nivel_estimado_riesgo)

