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

-Alerta Critica (Cuando el uso de cpu y el uso de ram superan el 85% y 80% respectivamente)

-Alerta de Mantenimiento (Cuando el espacio libre es inferior a 10GB y la cantidad de procesos activos supera los 250)

-Alerta de firewall (Cuando el mismo se encuentra desactivado)

-Uso normal del servidor (Cuando el uso de cpu y ram se encuentran dentro del rango 40%-70%)

-Alerta de escalar recurso (Si el servidor es de tipo WEB, hay mas de 100 usuarios conectados y el uso de cpu supera el 75%) 

-Promedio de uso por proceso () [REVISAR EN CODIGO]

-Recursos