Sistema de Diagnostico de Servidor
*****************************************************************************
Trabajo Practico Integrador | Programacion 1
*****************************************************************************
Equipo 2: 

Fabricio Maidana 

    Jorge Perdomo 

        Fleitas Agustin 

            Lourdes Luna Privitera 

                Ivan Caceres   
*****************************************************************************
Objetivo General:
Desarrollar un sistema por consola que: 

-Procese múltiples datos relacionados con la configuración de un servidor. 

-Evalúe reglas lógicas. 

-Detecte estados de riesgo, errores o configuraciones mejorables. 

-Genere recomendaciones automáticas de administración. 
*****************************************************************************
Reglas implementadas:

-Alerta Critica: 
Cuando el uso de cpu y el uso de ram superan el 85% y 80% respectivamente.

-Alerta de Mantenimiento:
Cuando el espacio libre es inferior a 10GB y la cantidad de procesos activos 
supera los 250.

-Alerta de firewall:
Cuando el mismo se encuentra desactivado.

-Uso normal del servidor:
Cuando el uso de cpu y ram se encuentran dentro del rango 40%-70%.

-Alerta de escalar recurso:
Si el servidor es de tipo WEB, hay mas de 100 usuarios conectados y el 
uso de cpu supera el 75%.

-Promedio de uso por proceso:
Calcula el promedio de uso por proceso si la cantidad de recursos por proceso 
es mayor a 3 y el uso de cpu o ram es mayor a 70 .

-Alerta de recursos: 
Cuando los recursos disponibles son menores a 20 y el ratio de recursos por usuario 
es mayor a 5 y el riesgo previo es alto o critico.

-Alerta de espacio minimo para Windows:
Cuando el servidor es Windows y en el espacio libre en disco es menor a 20GB.
*****************************************************************************
Ejemplo de Salida:

  💻 Diagnóstico del Servidor: Trabajo Integrador
  👤 Administrador: IvanCa24

  Estado general: Estado del sistema en leve estres (Medio)

  Problemas detectados:
  - Windows Server con solo 2500 GB libres. Mínimo recomendado: 20 GB.
  - Sistema operando en rango normal.

  Recomendaciones:
  ✓ Liberar almacenamiento o ampliar el volumen de disco.
  ✓ Continuar monitoreo de rutina, no se requiere acción.

