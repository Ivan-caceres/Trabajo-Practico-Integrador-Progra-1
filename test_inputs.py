#from inputs import *
from inputs import (
    ingresar_uso_cpu,
    ingresar_uso_ram,
    ingresar_espacio_libre_disco,
    ingresar_usuarios_conectados,
    ingresar_cantidad_procesos_activos,
    ingresar_sistema_operativo,
    ingresar_estado_firewall,
    ingresar_tipo_servidor,
    ingresar_nombre_servidor,
    ingresar_nombre_administrador
)


uso_cpu = ingresar_uso_cpu()
uso_ram = ingresar_uso_ram()
espacio_libre_disco = ingresar_espacio_libre_disco()
usuarios_conectados = ingresar_usuarios_conectados()
cantidad_procesos_activos = ingresar_cantidad_procesos_activos()

sistema_operativo = ingresar_sistema_operativo()
estado_firewall = ingresar_estado_firewall()
tipo_servidor = ingresar_tipo_servidor()

nombre_servidor = ingresar_nombre_servidor()
nombre_administrador = ingresar_nombre_administrador()

