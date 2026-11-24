# TRL-1 · ACTIVIDAD GRUPAL 1
### Principios científicos y oportunidades tecnológicas
### Team_pro · Procesos de Innovación en Ingeniería · 2026-II · Ingeniería Biomédica, UPCH

> **Propuesta de solución (idea base):** aplicación web progresiva (PWA) que registra los eventos de cada equipo biomédico y sigue funcionando sin internet (`Alternativa_Elegida_y_Boceto.md`). Las referencias **A01–A13** y **PAT01–PAT06** son las del proyecto (`Usuario_e_Insight.md`, `MATRICES.md`, `PATENTE.md`); **ENT-LV P#** es la pregunta número # del informe de la entrevista al Ing. Luis Vilcahuaman.

---

## 1. ¿Qué principios científicos consideran más importantes para su propuesta solución?

| # | PRINCIPIO | EN QUÉ CONSISTE | QUÉ PARTE DEL PROBLEMA ATIENDE | FUENTE |
| --- | --- | --- | --- | --- |
| 1 | **Confiabilidad del equipo y los atributos que la determinan** | La condición de un equipo médico no se reduce a "funciona o no": una revisión sistemática la describe con 8 categorías de atributos (características, función, requerimiento de mantenimiento, desempeño, riesgo y seguridad, disponibilidad o preparación, utilización y costo). | Sin registrar esas dimensiones no hay base para decidir qué atender. Sin un responsable de mantenimiento, un equipo diseñado para 7 años puede durar 3 o 4. | A01; ENT-LV P6 |
| 2 | **Mantenimiento preventivo y predictivo** | El preventivo sigue las recomendaciones del fabricante (equipos de tecnología antigua); el predictivo usa datos en tiempo real y aprendizaje automático (equipos de alta tecnología). Los equipos actuales traen sensores internos (vibración, temperatura, picos de corriente) que permiten el autodiagnóstico. | Define qué datos conviene registrar de cada equipo. En el Perú la norma solo exige el preventivo, y la evidencia de despliegue real en hospitales sigue siendo limitada. | A02; ENT-LV P17; PAT06 |
| 3 | **Decisión multicriterio y gestión por riesgo** | Modelos como AHP, TOPSIS y GRA-PCA combinan criterios técnicos, clínicos, de seguridad, financieros y de desempeño. En la práctica hospitalaria se usa una matriz por clases de riesgo (1 a 4): primero el riesgo directo para la vida del paciente y después el costo y el impacto asistencial. | Decidir qué equipo atender primero cuando varios fallan a la vez. | A03; ENT-LV P14, P15 |
| 4 | **Trazabilidad: registro de cada evento del equipo** | En el estándar internacional, el inventario registra cada evento (falla, mantenimiento, reparación) en el momento en que ocurre, como la historia clínica del equipo. En el Perú se usa como documento patrimonial. | Da memoria al equipo: es la base de toda decisión de mantenimiento. | ENT-LV P4, P9; PAT02 |
| 5 | **Computación en el borde y sincronización diferida** | Los datos se capturan y procesan en el propio dispositivo y se envían después, lo que reduce la dependencia de una conectividad continua. Se documenta en soluciones de salud para contextos de bajos recursos. | Que el registro no se interrumpa cuando falla el internet o la luz. | A06; ENT-LV P18 |
| 6 | **Interoperabilidad de datos en salud** | HL7/FHIR e ISO/IEEE 11073 son los estándares dominantes para intercambiar datos entre dispositivos y sistemas hospitalarios; FHIR usa una arquitectura REST/JSON que reduce la complejidad. | Permitiría integrar el registro con otros sistemas del hospital más adelante. | A05 |

---

## 2. Selección del principio más relevante y cómo ayuda a resolver el problema

### Criterio de selección

Puntuación de 0 a 2 en cada criterio, propuesta por el equipo para confirmarla en la sesión:

| PRINCIPIO | RESPONDE A UN DOLOR CONFIRMADO EN LA ENTREVISTA | ES CONDICIÓN NECESARIA DE LA IDEA BASE | SE PUEDE APLICAR EN NIVEL I–II (BAJO COSTO, SIN CONEXIÓN ESTABLE) | SE DIFERENCIA DE LO QUE YA EXISTE | TOTAL |
| --- | --- | --- | --- | --- | --- |
| 1 · Confiabilidad | 1 | 1 | 1 | 0 | 3 |
| 2 · Mantenimiento predictivo | 1 | 0 | 0 | 0 | 1 |
| 3 · Decisión por riesgo | 2 | 1 | 2 | 0 | 5 |
| 4 · Trazabilidad por eventos | 2 | 2 | 2 | 0 | 6 |
| **5 · Borde y sincronización diferida** | **2** | **2** | **2** | **1** | **7** |
| 6 · Interoperabilidad | 1 | 0 | 1 | 0 | 2 |

*Los principios 3 y 4 ya están definidos a nivel internacional (ENT-LV P8, P14: "no hay nada que inventar"), por eso puntúan 0 en diferenciación. El principio 5 recibe 1 y no 2 porque la diferencia es una hipótesis: los programas existentes operan en red (ENT-LV P13), pero no se verificó si ofrecen un modo sin conexión.*

### Principio seleccionado

> **Computación en el borde con sincronización diferida:** capturar y guardar cada dato en el propio dispositivo en el momento en que ocurre, y enviarlo después, cuando haya conexión.

### Cómo ayuda a resolver el problema

1. **El problema.** Cuando se cae el internet o la luz, el personal anota en papel y transcribe después, y se pierde información (ENT-LV P18). El inventario es uno de los instrumentos menos actualizados del sistema (ENT-LV P3). El resultado es que se decide sin un historial completo del equipo.
2. **Lo que aporta el principio.** El evento se guarda en el teléfono al instante y se sincroniza cuando vuelve la señal (A06: los dispositivos en el borde procesan los datos localmente antes de enviarlos).
3. **Lo que logra:**
   - El registro nunca queda bloqueado por la red, así que no hace falta anotar en papel ni transcribir.
   - El registro es inmediato porque no espera respuesta de la red; eso apoya el objetivo de menos de un minuto que el entrevistado verificó para el registro digital con casillas (ENT-LV P10).
   - Al sincronizar, la información queda consolidada para quien decide (ENT-LV P11).
   - Usa el teléfono del personal: no exige comprar equipos nuevos, coherente con un contexto de capacidad instalada inadecuada (A04).
   - Protege al principio 4: asegura que cada evento llegue a la historia del equipo.
4. **Lo que no resuelve.** No arregla la red eléctrica ni la de datos, que el entrevistado considera la causa de fondo (ENT-LV P19, P20); requiere un teléfono con batería; y no hay evidencia directa de que funcione para el registro de equipos biomédicos en nivel I–II, algo que falta validar con técnicos de esos establecimientos.

---

## 3. ¿Qué se sabe actualmente? ¿Cómo se aplica actualmente?

### Sobre el principio seleccionado y su contexto

| QUÉ SE SABE | CÓMO SE APLICA HOY | LÍMITE PARA NIVEL I–II | FUENTE |
| --- | --- | --- | --- |
| En contextos de bajos recursos, las soluciones de salud con sensores suelen apoyarse en dispositivos "edge" que filtran y procesan datos localmente antes de enviarlos; también se documentan kioscos de salud con sensores que permiten acceso remoto vía nube cuando la conexión es intermitente. | En soluciones de salud digital para bajos recursos, según una revisión de literatura. | Se documenta para soluciones de salud en general, no específicamente para el registro de equipos biomédicos. | A06 |
| Existen programas de gestión de mantenimiento (CMMS/IMMIS) de unos US$ 500 anuales por licencia, que operan en red y permiten que cientos de técnicos registren desde sus celulares. | En clínicas privadas hay avances; en hospitales públicos aún no se aplica por falta de regulación. | Dependen de la red y no se aplican en el sector público. | ENT-LV P11, P13 |
| En el estándar internacional, el inventario registra cada evento del equipo en el momento en que ocurre, de forma informatizada y sin papel. | En el Perú se usa como documento patrimonial que se actualiza una vez al año; la gestión depende de procesos manuales sin sistema estandarizado. | La práctica local está lejos del estándar. | ENT-LV P3, P4, P9; A13 |
| En el estándar mundial, los equipos médicos se conectan directamente a la red de datos del hospital y transfieren la información sin intervención manual. | En el Perú el internet se cae y la red eléctrica es inestable; el personal anota en papel y luego transcribe. | Depende de una infraestructura que no es estable. | ENT-LV P18 |
| Los equipos se clasifican por una matriz de riesgo en clases 1 a 4; tiene máxima prioridad el equipo cuya falla puede poner en riesgo la vida del paciente. | Los hospitales peruanos no saben aplicar estos criterios por normas incompletas y desactualizadas. | Aplicar los criterios depende de la normativa del Ministerio de Salud. | ENT-LV P14, P15, P16 |
| HL7/FHIR e ISO/IEEE 11073 son los estándares dominantes para intercambiar datos entre dispositivos y sistemas hospitalarios. | Se usan internacionalmente; es probable que los hospitales públicos de menor nivel no los hayan adoptado (supuesto). | Podrían dificultar integrar un sistema nuevo con los existentes. | A05 |

### Estado de la técnica en patentes

Las patentes se usan como antecedentes tecnológicos, no como prueba de eficacia.

| PATENTE | QUÉ APLICA | LÍMITE PARA NIVEL I–II |
| --- | --- | --- |
| PAT01 · ES2927525T3 | Identifica el dispositivo con NFC o chip y controla la cantidad de usos. | Controla solo los usos; no registra fallas, mantenimiento ni inventario. |
| PAT02 · EP3103099A4 | Gestiona el ciclo de vida y el flujo de mantenimiento de dispositivos reutilizables. | Depende de la carga manual de datos en cada paso. |
| PAT04 · US7518502B2 | Rastrea y localiza activos con radiofrecuencia. | Exige una red de antenas y receptores, con alto costo de despliegue. |
| PAT06 · US11404145B2 | Mantenimiento predictivo con inteligencia artificial a partir de telemetría continua. | Exige sensores integrados y conexión estable; inviable sin conectividad. |

### Lo que todavía no se sabe

- No hay evidencia directa, en las fuentes revisadas, de sincronización diferida aplicada específicamente al registro de equipos biomédicos.
- No se verificó si los programas de gestión existentes ofrecen un modo sin conexión.
- Falta saber cuántos técnicos de nivel I–II usan un teléfono propio en su trabajo (pendiente de entrevistas).

---

## Referencias de los códigos usados

| CÓDIGO | FUENTE | DATO ESPECÍFICO USADO | ARCHIVO DEL PROYECTO |
| --- | --- | --- | --- |
| A01 | Revisión sistemática, *Frontiers in Public Health*, 2021 (DOI 10.3389/fpubh.2021.753951) | 8 categorías de atributos para evaluar la confiabilidad de un equipo. | `Usuario_e_Insight.md`, fila 1 |
| A02 | Estudios en hospital (PMC5058563; PMC13121388) | Mantenimiento preventivo según el fabricante y predictivo con datos y aprendizaje automático; evidencia de despliegue real limitada. | `Usuario_e_Insight.md`, fila 2 |
| A03 | *Frontiers in Medicine*, 2023 (DOI 10.3389/fmed.2023.1239795); PMID 40621426 | Modelos AHP, TOPSIS y GRA-PCA que combinan criterios técnicos, clínicos, de seguridad, financieros y de desempeño. | `Usuario_e_Insight.md`, fila 3 |
| A04 | MINSA/OPMI, *Diagnóstico de brechas* | 97 % de establecimientos de primer nivel y 236 de 247 hospitales con capacidad instalada inadecuada al cierre de 2020. | `Usuario_e_Insight.md`, fila 4 |
| A05 | PMC8367140; arXiv:1812.06327 | HL7/FHIR e ISO/IEEE 11073 como estándares dominantes; FHIR con API REST/JSON. | `Usuario_e_Insight.md`, fila 5 |
| A06 | arXiv:2205.10913 | Dispositivos "edge" que procesan datos localmente; kioscos con acceso por nube ante conexión intermitente. | `Usuario_e_Insight.md`, fila 6 |
| A13 | Sandoval et al., IEEE RFID-TA 2023 | La gestión de equipos en el Perú depende de procesos manuales, sin sistema estandarizado. | `MATRICES.md`, evidencia E8 |
| PAT01, PAT02, PAT04, PAT06 | ES2927525T3; EP3103099A4; US7518502B2; US11404145B2 | Función y limitación de cada patente. | `PATENTE.md`, sección B |
| ENT-LV | Entrevista al Ing. Luis Vilcahuaman (PUCP/UPCH), más de 25 años de experiencia | P3, P4, P6, P8, P9, P10, P11, P13, P14, P15, P16, P17, P18, P19, P20 del informe. | `Resumen_Entrevista_Luis_Vilcahuaman.pdf` |
