# INSTRUMENTO 1 · BÚSQUEDA Y COMPARACIÓN DE TRES PATENTES
Este instrumento reúne la estrategia de búsqueda y la matriz de patentes. No se requiere una ficha adicional por cada documento.
## A. Foco técnico y estrategia
| EQUIPO | CARRERA | RETO / NECESIDAD | ODS RELACIONADO |
| --- | --- | --- | --- |
| Team_pro | Ingeniería Biomédica | Dificultades organizacionales y técnicas en establecimientos de salud para gestionar el mantenimiento, la disponibilidad, el inventario y el seguimiento de tecnovigilancia de equipos biomédicos en el Perú. | ODS 3 (Salud y bienestar) |
| FUNCIÓN | OBJETO | CONTEXTO | RESTRICCIÓN |
| Gestionar y vigilar | Equipos Médicos | Establecimientos de salud y entornos hospitalarios | Bajo costo de despliegue, interfaz simplificada y operabilidad en entornos con conectividad limitada. |
## Términos y consultas ejecutadas
| PLATAFORMA | CONSULTA EXACTA | FILTROS / IPC-CPC SI APLICA | FECHA | RESPONSABLE |
| --- | --- | --- | --- | --- | 
| Google Patents | ("medical device management" OR "biomedical equipment tracking") AND ("maintenance" OR "vigilance" OR "usage count") | CPC: G16H40/40 (Gestión o mantenimiento de equipos médicos) | 05/09/2026 | Ailen Rosario Baldera Echevarria |
| Espacenet | ctxt="medical device" AND ctxt = "management system" AND ctxt = "maintenance" | IPC:G16H40/40, G16H40/20  | 05/09/2026 | Sergio Andre Garcia Zapata |
| PATENTSCOPE] | FP:("medical system control" AND "device status" AND "maintenance") | Filtro: Publicaciones en el área de salud/informática | 05/09/2026 | Joel David Mendoza Choquepata |


## B. Matriz de tres patentes comparables 

| PATENTE / ENLACE | PRIORIDAD - SOLICITANTE - ESTADO VISIBLE | FUNCIÓN | PRINCIPIO TÉCNICO | CONDICIONES / DEPENDENCIAS | LIMITACIÓN O BRECHA |
| --- | --- | --- | --- | --- | --- |
| Patente 1 — ES2927525T3 — Sistema para gestionar el uso de dispositivos médicos - https://patents.google.com/patent/ES2927525T3/en)] | Prioridad: 20/05/2015 - THD SpA - Activa | Registrar los ciclos de uso y restringir/bloquear el funcionamiento de aparatos médicos según los límites preestablecidos.| Identifica el dispositivo de forma electrónica (NFC o chip), registra y calcula las veces que se ha utilizado y envía una señal para autorizar o bloquear el equipo según las reglas fijadas. | Necesita que el dispositivo tenga un identificador (RFID o memoria) y un lector que verifique si el equipo ya alcanzó su límite de uso antes de funcionar. | Se enfoca únicamente en el control de usos para evitar la reutilización, sin registrar fallas técnicas, mantenimiento preventivo, disponibilidad ni el control de inventario de los equipos en el hospital. |
| Patente 2 - EP3103099A4 - Device management system -  https://patents.google.com/patent/EP3103099A4/en?oq=EP3103099A4 | Prioridad: 07/02/2014  07/02/2014 – Smartline Machinery Pty Ltd – Retirada | Gestionar, monitorear y rastrear el ciclo de vida, estado de desinfección y flujo de mantenimiento de dispositivos médicos reutilizables. | Identificación y gestión digital de dispositivos mediante información asociada a cada equipo. | Requiere dispositivos identificables, un sistema de gestión y registro de las operaciones realizadas sobre ellos. | A pesar de que gestiona la disponibilidad y el flujo del equipo, depende de la carga manual de datos en cada paso y no se conecta con un sistema de alertas de tecnovigilancia ni registros de fallas mecánicas/electrónicas. |
| Patente 3 - CN101833290B - Portable and programmable medical device system - https://patents.google.com/patent/CN101833290B/en?oq=CN101833290B | 17/02/2009 – Tyco Healthcare Group LP – Activo | Sistema médico portátil y programable que permite seleccionar y ejecutar diferentes programas de funcionamiento en un dispositivo médico portátil mediante una unidad de acoplamiento. | Seleccionar y ejecutar programas de operación en un dispositivo médico portátil. | Requiere acoplamiento del dispositivo, controlador programable y al menos dos programas de operación; la configuración se mantiene tras el desacoplamiento. | Se centra exclusivamente en el control y programación de parámetros de un solo equipo portátil, sin gestionar el historial global de fallas, mantenimiento ni disponibilidad del parque hospitalario.|


# INSTRUMENTO 2 - BRECHAS Y PREGUNTAS DE DESK RESEARCH

| BRECHA / LIMITACION OBSERVADA | PREGUNTA DE DESK  RESEARCH | FUENTE SECUNDARIA A CONSULTAR | QUÉ NECESITAMOS APRENDER | RESPONSABLE |
| --- | --- | --- | --- | --- |
| La Patente 2 requiere registro manual en cada etapa del ciclo del equipo, lo que puede saturar al personal de salud en hospitales con alta demanda. | ¿Cuáles son los principales obstáculos operativos que enfrenta el personal de salud y los ingenieros clínicos al documentar de manera manual el mantenimiento de los equipos? | Articulo / norma / dato oficial / reporte | dato, condición o criterio | nombre |
|La Patente 1 bloquea el uso por cantidad de ciclos, pero no genera alertas automáticas de tecnovigilancia tras detectarse un evento adverso o fallo recurrente. | ¿Qué formatos y plazos exige formalmente la DIGEMID / CENAFyT para el reporte normativo de incidentes adversos en dispositivos médicos? | Articulo / norma / dato oficial / reporte | Los requisitos mínimos de información que una herramienta tecnológica debe recopilar para automatizar reportes de tecnovigilancia. | nombre |
| La Patente 3 requiere infraestructura de acoplamiento de hardware específica, lo cual es inviable para la gran variedad de marcas y modelos en hospitales públicos. | ¿Cuál es el grado de heterogeneidad (variedad de marcas, modelos y antigüedad) de los equipos biomédicos en los hospitales del sector público peruano? | Articulo / norma / dato oficial / reporte  | Identificar si la solución debe ser independiente del hardware (operar a través de software o etiquetas estándar como QR/NFC) con el fin de ser compatible con cualquier dispositivo. | nombre |
| Ninguna de las patentes ofrece un sistema integral de bajo costo que unifique inventario, control de fallas y estado operativo para hospitales con recursos limitados. | ¿Qué porcentaje de establecimientos de salud públicos en el Perú cuenta con un área formal o presupuesto asignado para la gestión de tecnología biomédica? | Articulo / norma / dato oficial / reporte | Evaluar la factibilidad económica y la necesidad de una plataforma que sea económica y de fácil implementación. | nombre |

# Sintesis del equipo
| PREGUNTA | RESPUESTA BREVE DEL EQUIPO | RESPUESTA BREVE DEL EQUIPO | 
| --- | --- | --- | 
| [Derivada del Instrumento 1] | Pregunta de investigación | Articulo / norma / dato oficial / reporte | dato, condición o criterio | nombre |
| [Derivada del Instrumento 1] | Pregunta de investigación | Articulo / norma / dato oficial / reporte | dato, condición o criterio | nombre |


