
uso_cpu = int(input("Ingrese el uso de su CPU : "))
while uso_cpu < 0 or uso_cpu > 100:
    uso_cpu = int(input("Error. Ingrese un valor entre 0 y 100: "))

uso_ram = float(input("Ingrese memoria RAM (4,8,16,32,128): "))
while uso_ram != 4 and uso_ram != 8 and uso_ram != 16 and uso_ram != 32 and uso_ram != 128 :
    uso_ram = int(input("Error. Reingrese memoria RAM (4,8,16,32,128): "))

espacio_libre_disco = float(input("Ingrese cuanto Espacio libre hay en el disco (GB): "))
while espacio_libre_disco < 0 or espacio_libre_disco > 1000 :
    espacio_libre_disco = int(input("Error. Ingrese un valor entre 0 y 1000: "))

usuarios_conectados  = int(input("Ingrese Cantidad de usuarios conectados: "))
while usuarios_conectados < 0 or usuarios_conectados > 100:
    usuarios_conectados = int(input("Error. Reingrese un valor entre 0 y 100: "))

cantidad_procesos_activos = int(input("Ingrese Cantidad de Cantidad de procesos activos: "))
while cantidad_procesos_activos < 0 or cantidad_procesos_activos > 1000 :
    cantidad_procesos_activos = int(input("Error. Ingrese cantidad de procesos activos 0 y 1000 : "))

sistema_operativo = input("Seleccione su sistema operativo linux / windows Server: ")
while sistema_operativo != "linux" and sistema_operativo != "windows Server" :
    sistema_operativo = input("Error. Seleccione un sistema operativo valido linux / windows Server: ")
    
estado_firewall = input("Estado del firewall Activo / Inactivo:  ")
while estado_firewall != "Activo" and estado_firewall != "Inactivo" :
    estado_firewall = input("Error. REINGRESE Estado del firewall Activo / Inactivo: ")

tipo_servidor = input("Seleccione su tipo de servidor Web / Base de datos / Archivos: ")
while tipo_servidor != "Web" and tipo_servidor != "Base de datos" and tipo_servidor != "Archivos" :
    tipo_servidor = input("Error. REINGRESE tipo de servidor Web / Base de datos / Archivos: ")

nombre_servidor = input("Ingrese nombre del servidor: ")
while nombre_servidor == ""  :
    nombre_servidor = input("Error. REINGRESE nombre del servidor: ")

nombre_administrador = input("Ingrese nombre del administrador responsable: ")
while nombre_administrador == ""  :
    nombre_administrador = input("Error. REINGRESE nombre del administrador responsable: ")

