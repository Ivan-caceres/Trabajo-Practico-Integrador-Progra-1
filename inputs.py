'''
Categóricos (3 mínimo). Opciones cerradas. Ejemplos: 
Sistema operativo (Linux / Windows Server) 
Estado del firewall (Activo / Inactivo) 
Tipo de servidor (Web / Base de datos / Archivos) 
Cadenas (2 mínimo) Ejemplos: Nombre del servidor / Nombre del administrador responsable 
10 INPUTS: Numéricos 5, Categóricos 3 y Cadenas 2 
VALIDACIONES de ingreso: solo números, coincidencia de opciones  y mínimo un espacio ¿?
'''
#validar con un while el ingreso de los 10 dtos, si responde una, pasa a la otra 
#validar que se ingresen numeros





uso_cpu = int(input("Ingrese cuanto es el uso de su CPU (%) "))
while uso_cpu < 0 or uso_cpu > 100:
    uso_cpu = int(input("Error. Ingrese un valor entre 0 y 100: "))
     


uso_cpu = int(input("Ingrese cuanto es el uso de su CPU (%) "))

uso_ram = float(input("Ingrese cuanto es el de memoria RAM (%) "))

espacio_libre_disco = float(input("Ingrese cuanto Espacio libre hay en el disco (GB) "))

usuarios_conectados  = int(input("Ingrese Cantidad de usuarios conectados "))

cantidad_procesos_activos = int(input("Ingrese Cantidad de Cantidad de procesos activos "))

#validar que se seleccionen las opciones
sistema_operativo = input("Seleccione su sistema operativo (linux / windows Server) ")
while sistema_operativo == "linux" or sistema_operativo == "windows Server" :
    sistema_operativo = input("Error. Seleccione un sistema operativo valido: ")
    
estado_firewall = input("Estado del firewall Activo / Inactivo  ")
while estado_firewall == "Activo" or estado_firewall == "Inactivo" :
    estado_firewall = input("Error. REINGRESE Estado del firewall Activo / Inactivo ")

tipo_servidor = input("Seleccione su tipo de servidor (Web / Base de datos / Archivos) ")
while tipo_servidor == "Web" or tipo_servidor == "Base de datos" or tipo_servidor == "Archivos" :
    tipo_servidor = input("Error. REINGRESE Estado del firewall Activo / Inactivo ")
    
#validar cadena 
nombre_servidor = input("Ingrese nombre del servidor ")
nombre_administrador = input("Ingrese nombre del administrador responsable ")
