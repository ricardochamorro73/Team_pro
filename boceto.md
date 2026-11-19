# ALTERNATIVA ELEGIDA Y BOCETO BASE
### Team_pro · Procesos de Innovación en Ingeniería · 2026-II · Ingeniería Biomédica, UPCH

> Decisión tomada a partir de las 10 ideas ganadoras de `Idear_Ficha_Design_Thinking.md` y del informe de la entrevista al **Ing. Luis Vilcahuaman** (docente e investigador de ingeniería biomédica, PUCP/UPCH). Las referencias **P1–P20** son los números de pregunta del informe de la entrevista.

---

## 1. Qué dijo la entrevista y qué implica

| HALLAZGO | PREGUNTA | QUÉ IMPLICA PARA EL PROYECTO |
| --- | --- | --- |
| En el estándar internacional, el inventario registra cada evento del equipo, como una historia clínica. En el Perú se usa solo como documento patrimonial y casi no se actualiza. | P3, P4 | La solución debe ser un registro de eventos por equipo, no un inventario contable. |
| Registrar debe hacerse en el momento en que ocurre, de forma informatizada y sin papel. Llevar registros en papel para transcribirlos después "nunca funciona". | P9, P12 | Se descarta la idea de empezar en papel. |
| En ensayos de laboratorio, el registro informatizado toma menos de un minuto con plantillas de casillas y datos puntuales. | P10 | El registro debe ser corto y por casillas. |
| Ya existen programas de gestión de mantenimiento (CMMS/IMMIS) a unos US$ 500 anuales por licencia, que operan en red desde celulares. | P13 | Hay una alternativa comercial; hay que diferenciarse (ver límites). |
| Se prioriza con una matriz de riesgo por clases (1 a 4): primero el riesgo para la vida del paciente, luego el impacto en costos y en la atención. Los hospitales peruanos no saben aplicarla por normas incompletas. | P14, P15 | La priorización debe usar esos criterios, no pesos inventados por el equipo. |
| En el Perú el internet se cae y la red eléctrica es inestable; el personal anota en papel y luego transcribe, con pérdida de información. | P18 | Dolor confirmado: el registro debe tolerar cortes. |
| Que un equipo funcione sin internet ni electricidad "no tiene mucho sentido técnico"; una conexión intermitente es una falla de infraestructura que debe corregirse en su causa. | P19, P20 | La herramienta protege el registro ante cortes, no reemplaza arreglar la infraestructura. |
| En la formalidad nadie es responsable del equipo: el "encargado" no tiene autoridad. Sin responsable, un equipo de 7 años puede durar 3 o 4, los pacientes pierden atención y el hospital pierde ingresos. | P6, P7 | Supuesto del responsable de mantenimiento apoyado. |

## 2. Qué le pasa a cada alternativa ganadora

| # | ALTERNATIVA | EFECTO | MOTIVO |
| --- | --- | --- | --- |
| 1 | Formato estandarizado de 8 categorías (A01) | Se ajusta | Debe ser digital y con casillas (P9, P10), no en papel. |
| 2 | Código QR en cada equipo | Sin evidencia nueva | La entrevista no lo menciona; queda como mejora posterior. |
| 3 | Panel visual de estado por colores | Se refuerza | El nivel gerencial consulta datos consolidados en tiempo real (P11). |
| 4 | Índice de condición y orden de prioridad | Se reformula | Debe usar la clase de riesgo, luego costo e impacto asistencial (P14). |
| 5 | Registro solo de eventos que cambian el estado | Se refuerza | El inventario registra cada evento del equipo (P4, P9). |
| 6 | Formulario con valores por defecto | Se refuerza | Coincide con las plantillas de casillas de menos de un minuto (P10). |
| 7 | Registro integrado en la entrega de turno | Se debilita | El entrevistado pide registrar al instante, no por lote (P9). |
| **8** | **Aplicación web progresiva (PWA) sin conexión** | **Se refuerza, con un matiz** | **Responde al problema de los cortes (P18); el matiz está en P19 y P20.** |
| 9 | Versión en papel primero | Se descarta | Contradice P9 y P12. |
| 10 | Sensor de bajo costo en equipos críticos | Se pospone | Los equipos modernos ya traen sensores y la norma solo exige mantenimiento preventivo (P17). |

## 3. Alternativa elegida: aplicación web progresiva (PWA) sin conexión

*(Origen: Pregunta 3 · idea 5-1 de la ficha de Idear.)*

**Por qué esta:**
1. **Es la única que ataca el problema confirmado.** Hoy los cortes obligan a anotar en papel y transcribir después, con pérdida de información (P18); la PWA guarda en el teléfono y envía cuando vuelve la señal, y cumple la exigencia de "sin papel" (P9, P12).
2. **Es la base de las demás ideas reforzadas.** Las ideas 3, 5 y 6 funcionan como pantallas dentro de la PWA: registro corto por casillas (6), historia por evento (5) y vista de lo urgente (3, con el orden de la 4 reformulada).
3. **No exige comprar equipos ni sensores.** Funciona en el teléfono del personal, coherente con la restricción de bajo costo y con el contexto de capacidad instalada inadecuada (A04).
4. **Puede diferenciarse del software comercial** si es sin conexión y de código abierto (idea 5-4 de la Pregunta 3). Esto es una hipótesis: falta verificar si los programas existentes funcionan sin conexión.

## 4. Boceto base

![Boceto de la solución base: cuatro pantallas y diagrama de bloques](Boceto_Solucion_Base.png)

| PANTALLA | QUÉ MUESTRA | VIENE DE |
| --- | --- | --- |
| 1 · Lista priorizada | Equipos ordenados por riesgo y estado, con aviso de registros pendientes. | Ideas 3 y 4 (reformulada), P14 |
| 2 · Historia del equipo | Línea de tiempo de eventos: falla, revisión, espera de repuestos. | Idea 5, P4, P9 |
| 3 · Registro en menos de 1 minuto | Equipo ya elegido, tipo de evento, casillas, fecha y hora automáticas. | Idea 6, P10 |
| 4 · Sincronización | Registros guardados en el teléfono y envío automático al volver la señal. | Idea 8, P18 |

**Diagrama de bloques:**

| ENTRADAS | PROCESAMIENTO | SALIDAS | MÓDULOS |
| --- | --- | --- | --- |
| Enfermería y técnicos registran cada evento con casillas. | Guarda en el teléfono, ordena por riesgo y estado, y mantiene una cola de envío. | Historia de cada equipo, lista priorizada y vista para quien decide. | Aplicación web progresiva, almacenamiento local en el teléfono y sincronización cuando hay señal. |

*Los nombres de equipos y los horarios del boceto son ejemplos ilustrativos.*

## 5. Efecto sobre los supuestos del proyecto

| SUPUESTO | RESULTADO | BASE |
| --- | --- | --- |
| Existe un responsable de mantenimiento | Apoyado: en la formalidad nadie es responsable. | P7 |
| Registrar compite con atender los equipos | Matizado: no compite si el registro es digital y breve, según ensayos de laboratorio. | P10 |
| Hoy se decide sin criterios explícitos | Apoyado en la práctica: los criterios existen, pero los hospitales no los aplican. | P14, P15 |
| Sensores, conectividad y electricidad son estables | Parcial: internet y electricidad inestables; sin dato sobre los equipos antiguos de nivel I–II. | P17, P18 |

## 6. Límites y pendientes

- **El entrevistado es un experto, no nuestro usuario.** Falta validar con técnicos de establecimientos de nivel I–II, sobre todo si el registro de menos de un minuto se cumple en campo y qué teléfonos usan.
- **Ya existen programas de pago (P13).** Hay que revisar si funcionan sin conexión y si ese costo es asumible en nivel I–II antes de afirmar que nos diferenciamos.
- **Clases de riesgo.** El informe menciona las clases 1 a 4 sin decir cuál es la de mayor riesgo; en el boceto se usó "riesgo alto" y "riesgo medio". Hay que confirmar la convención de la matriz que se adopte.
- **Correcciones a la ficha de Idear:** descartar la idea 9, reformular la idea 4 con la clase de riesgo, y cambiar el Insight 3 de "diseñar desde la carencia" a "diseñar para que tolere la carencia" (P19, P20).
- **Fuera del alcance del proyecto:** actualizar las normas y los reglamentos del sector, que el entrevistado considera una decisión política del MINSA (P16).

<img width="1600" height="1020" alt="WhatsApp Image 2026-11-18 at 21 46 16" src="https://github.com/user-attachments/assets/1696fefa-daee-418a-beef-99fd13ebe889" />
