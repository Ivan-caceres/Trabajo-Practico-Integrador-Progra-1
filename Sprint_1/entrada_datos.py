def datos_numericos():
    uso_cpu = int(input("Ingrese el uso actual de su CPU (%): "))
    uso_ram = int(input("Ingrese el uso actual de su RAM (%): "))
    espacio_libre = int(input("Ingrese el espacio libre en disco (GB): "))
    usuarios_conec = int(input("Ingrese la cantidad de usuarios conectados: "))
    cant_proc = int(input("Ingrese la cantidad de procesos activos: "))
    return uso_cpu, uso_ram, espacio_libre, usuarios_conec, cant_proc

def datos_categoricos():
    so = input("Sistema operativo(Linux / Windows Server): ")
    firewall = input("Estado del Firewall(Activo / Inactivo): ")
    tipo_serv = input("Tipo de servidor (Web / Base de datos / Archivos): ")
    return so, firewall, tipo_serv

def datos_cadenas():
    serv_name = input("Ingrese el nombre del servidor: ")
    adm_name = input("Ingrese su nombre de usuario con permisos de administrador: ")
    return serv_name, adm_name