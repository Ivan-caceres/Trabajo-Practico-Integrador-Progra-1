from entrada_datos import *
from calculo_variables import *
from motor_reglas import *

def mostrar_diagnostico():

    uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cant_procesos, so, firewall, tipo_serv, nombre_servidor, nombre_administrador = obtener_datos()

    carga_total, recursos_disponibles, uso_por_proc, ratio_user, nivel_riesgo, estado_general = calculo_variables
    (uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cant_procesos, tipo_serv)

    (alerta_critica, alerta_mantenimiento, alerta_seguridad, alerta_normal,
     alerta_web, alerta_proceso, alerta_recursos, alerta_disco,
     mensaje_critica, mensaje_mantenimiento, mensaje_seguridad, mensaje_normal,
     mensaje_web, mensaje_proceso, mensaje_recursos, mensaje_disco) = evaluar_reglas
    (uso_cpu, uso_ram, espacio_libre, usuarios_conectados, cant_procesos,
    so, firewall, tipo_serv, carga_total, recursos_disponibles, uso_por_proc, ratio_user, nivel_riesgo)

    print("=" * 55)
    print(f"  💻 Diagnóstico del Servidor: {nombre_servidor}")
    print(f"  👤 Administrador: {nombre_administrador}")
    print("=" * 55)
    print(f"\n  Estado general: {estado_general} ({nivel_riesgo})")

    print("\n  Problemas detectados:")
    if alerta_critica:
        print(f"  - {mensaje_critica}")
    if alerta_mantenimiento:
        print(f"  - {mensaje_mantenimiento}")
    if alerta_seguridad:
        print(f"  - {mensaje_seguridad}")
    if alerta_web:
        print(f"  - {mensaje_web}")
    if alerta_proceso:
        print(f"  - {mensaje_proceso}")
    if alerta_recursos:
        print(f"  - {mensaje_recursos}")
    if alerta_disco:
        print(f"  - {mensaje_disco}")
    if not any([alerta_critica, alerta_mantenimiento, alerta_seguridad,
                alerta_web, alerta_proceso, alerta_recursos, alerta_disco]):
        print("  - Sin problemas detectados.")
    if alerta_normal:
        print("  - Sistema operando en rango normal.")

    print("\n  Recomendaciones:")
    if alerta_critica:
        print("  ✓ Finalizar procesos no esenciales inmediatamente.")
    if alerta_mantenimiento:
        print("  ✓ Liberar espacio en disco y revisar procesos activos.")
    if alerta_seguridad:
        print("  ✓ Activar el firewall de inmediato.")
    if alerta_web:
        print("  ✓ Escalar recursos o activar balanceo de carga.")
    if alerta_proceso:
        print("  ✓ Identificar y optimizar los procesos más demandantes.")
    if alerta_recursos:
        print("  ✓ Reducir usuarios conectados o aumentar capacidad.")
    if alerta_disco:
        print("  ✓ Liberar almacenamiento o ampliar el volumen de disco.")
    if not any([alerta_critica, alerta_mantenimiento, alerta_seguridad,
                alerta_web, alerta_proceso, alerta_recursos, alerta_disco]):
        print("  ✓ Continuar monitoreo de rutina.")
    if alerta_normal:
        print("  ✓ Continuar monitoreo de rutina, no se requiere acción.")

    print("\n" + "=" * 55)

mostrar_diagnostico()