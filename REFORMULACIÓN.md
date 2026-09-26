# Hoja de trabajo | Control de encaje problema-usuario
### Team_pro · Semana 06 · Procesos de Innovación en Ingeniería · 2026-II

**Problema reformulado (POV 1):** el técnico o ingeniero biomédico responsable del mantenimiento en un establecimiento público de nivel I–II necesita conocer en cualquier momento la condición real de cada equipo para decidir qué atender primero.

| ESLABÓN | CÓDIGO Axx/PATxx | AFIRMACIÓN | RIESGO | PRÓXIMA VALIDACIÓN | DECISIÓN |
| --- | --- | --- | --- | --- | --- |
| Artículo/Patente/Dato | A01, A13; PAT02, PAT04, PAT06 | Existen estudios (Frontiers in Public Health 2021; Sandoval et al., IEEE RFID-TA 2023) y patentes (EP3103099A4, US7518502B2, US11404145B2) sobre evaluación y gestión de equipos médicos. | Bajo — fuentes revisadas por pares y patentes verificables. | — | Se mantiene. |
| Evidencia extraída | A01, A04, A06, A13 | El estado de un equipo se mide con 8 categorías (A01); 97 % de establecimientos de primer nivel tiene capacidad instalada inadecuada (A04); existen esquemas de baja dependencia de conectividad (A06); la gestión depende de procesos manuales (A13). | Medio — el dato de A04 es de 2020. | Confirmar si la brecha de infraestructura sigue vigente en 2026. | Se mantiene, con nota de vigencia. |
| Hallazgo | A01, A13 | No hay una forma común de registrar el estado del equipo; la gestión depende de procesos manuales sin estandarizar. | Medio — se apoya en una sola fuente técnica peruana (A13). | Contrastar A13 con una segunda fuente técnica si aparece. | Se mantiene con vigilancia. |
| Actor | — (A09 sugiere lo contrario) | El actor es el técnico o ingeniero biomédico (o quien haga sus veces) responsable del mantenimiento en un establecimiento de nivel I–II. | **Alto** — no hay dato nacional que confirme que ese responsable existe de forma formal en todos los establecimientos. | Entrevistar a 2–3 establecimientos de nivel I–II. | Pendiente de validar. |
| Insight | A01, A03, A13 | El registro disperso y sin estándar impide una vista completa del equipo para decidir qué atender primero. | Medio — es una hipótesis, no un hecho confirmado en campo. | Validar en entrevista si la dispersión es el obstáculo principal. | Se mantiene como hipótesis a probar. |
| POV | A01, A04, A06, A13; PAT04, PAT06 | El técnico/ingeniero biomédico de nivel I–II necesita conocer la condición real de cada equipo sin depender de sensores ni conexión continua. | Medio — la accesibilidad real al usuario aún no se ha probado. | Confirmar acceso a un establecimiento piloto para entrevista. | Pendiente de validar. |
| HMW | — (verificado en prueba de neutralidad, Semana 05) | Los 3 HMW (1.1–1.3) admiten varias familias de respuesta y no nombran una solución ni una tecnología. | Bajo. | — | Se mantiene. |
| Alcance | A04, A06 | El alcance se limita a establecimientos públicos de nivel I–II, sin telemetría propia ni decisiones clínicas. | Bajo. | — | Se mantiene. |

## Control de encaje

- [x] El usuario es específico y accesible — *específico sí; el acceso real aún está pendiente de validar.*
- [x] La necesidad aparece en evidencia convergente — A01, A02, A03, A04, A06, A08, A09, A13.
- [x] El contexto y las restricciones están declarados — nivel I–II, bajo costo, interfaz simple, conectividad limitada.
- [x] El problema no contiene una solución anticipada.
