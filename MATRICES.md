# MATRICES
## Hoja de trabajo 1 
### Pregunta y términos

| Equipo | Carrera | Reto o tema inicial | ODS candidato |
| :---: | :---: | :---: | :---: | 
| Team Pro | Ingeniería Biomédica | La ausencia de un sistema nacional de gestión biomédica y tecnovigilancia que ha permitido que los equipos médicos en el Perú se degraden sin control, limitando la capacidad de respuesta hospitalaria, reduciendo la eficiencia en el acceso a tecnologías críticas y profundizando la inequidad en la atención de salud. | ODS 17 |



### Pregunta de evidencia

| ¿Qué evidencia describe la obsolescencia de los equipos biomédicos en los hospitales públicos del Perú dentro de la gestión tecnológica hospitalaria, cuáles son sus causas o consecuencias y qué cambio se relaciona con la implementación de un sistema nacional de tecnovigilancia y mantenimiento inteligente? |
| --- |

### Tabla de conceptos y términos
| BLOQUE | ESPAÑOL | INGLÉS / SINÓNIMOS | TÉRMINO CONTROLADO O DE ÍNDICE | APORTE A LA CONSULTA |
| :---: | :---: | :---: | :---: | :---: |
| Actor / sistema | Sistema Peruano de Farmacovigilancia y Tecnovigilancia (DIGEMID/CENAFyT); áreas de ingeniería clínica/biomédica hospitalaria | Medical device vigilance system; clinical/biomedical engineering department; Health Technology Management (HTM) | MeSH: Product Surveillance, Postmarketing; Equipment and Supplies; IEEE keyword: Medical device management | Define el sistema institucional y el área técnica responsables |
| Brecha / fenómeno | Resistencia institucional y falta de capacidades técnicas para adoptar gestión de tecnología biomédica | Institutional resistance; technology adoption barriers; technical capacity gap | MeSH: Organizational Innovation; Diffusion of Innovation; IEEE keyword: Technology adoption barriers, Health technology management | Es el núcleo organizacional-técnico del problema |
| Contexto | Hospitales públicos y privados del Perú; sistema de salud fragmentado en subsectores | Peru; public hospitals; low-resource healthcare setting | MeSH: Peru [Geographic]; Public Hospitals | Delimita el ámbito institucional y geográfico |
| Consecuencia | Inoperatividad de equipos médicos, subregistro de incidentes adversos, retraso diagnóstico | Equipment downtime; underreporting of adverse events; diagnostic delay  | MeSH: Equipment Failure; Patient Safety | Acota el impacto medible que se busca documentar | 

### Consultas exactas que se ejecutarán
| BASE | CONSULTA COMPLETA | FILTROS PLANIFICADOS | RESPONSABLE |
| --- | --- | --- | --- |
| PubMed / MEDLINE | ("health technology management" OR "medical equipment management") AND ("institutional resistance" OR "technical capacity" OR "technology adoption") AND Peru | Años 2019–2026; artículos y revisiones | [Nombre] |
| IEEE Xplore | ("biomedical equipment management" OR "medical device surveillance") AND ("adoption barriers" OR "institutional") AND (Peru OR "developing country") | Años 2019–2026; conference papers y journals; tema "Health informatics / biomedical engineering" | [Nombre] |

## Hoja de trabajo 2 
## 🔎 **Registro de búsqueda y triage**

| Fecha | Base | Consulta exacta | Filtros | Revisados / incluidos | Resp. |
|---|---|---|---|---|---|
| 30/08/2026 | Búsqueda exploratoria (prensa especializada + repositorios abiertos) | interoperabilidad historia clínica electrónica Perú fragmentación | Últimos 6 años (2020–2026) | 15 / 7 | `[Nombre]` |
| 30/08/2026 | PubMed | ("electronic health records"[MeSH] OR "health information interoperability") AND (Peru) AND (fragmentation OR "health information exchange") | 2019–2026 | 9 / 0 — no aparecen artículos Perú-específicos indexados en PubMed; los resultados son de interoperabilidad de HCE en general (EE.UU., Europa). El estudio peruano más relevante (Mauricio et al., 2024) está indexado en Scopus, no en PubMed | `[Nombre]` |
| 30/08/2026 | IEEE Xplore | ("interoperability" AND "electronic health record" AND "Peru") | 2019–2026 | 6 / 1 — confirma el mismo estudio ya usado en la matriz (Mauricio et al., 2024, iJOE, con arquitectura basada en HL7 FHIR y blockchain) | `[Nombre]` |
| 30/08/2026 | Scopus | TITLE-ABS-KEY(interoperability AND "electronic health record" AND Peru) | 2019–2026 | Sin acceso institucional a Scopus desde aquí — pendiente de correr con tu cuenta UPCH; el estudio de Mauricio et al. (2024) sí está indexado ahí | `[Nombre]` |
| 30/08/2026 | SciELO / Google Scholar | interoperabilidad salud digital Perú historia clínica | 2019–2026, solo Perú/LatAm | 7 / 1 — confirma la revisión de TecnoHumanismo (Lima, 2022) ya incluida en la matriz | `[Nombre]` |

---

## 🧪 **Triage de fuentes candidatas**

| ID | TÍTULO CORTO / AÑO | TIPO DE FUENTE | DECISIÓN | JUSTIFICACIÓN | 
| --- | --- | --- | --- | --- |
| S1 | "El Rol de la Tecnología en la Gestión de la Salud en Hospitales Públicos" (SAGA, 2025)  | Revisión científica (revista multidisciplinaria) | Incluir | Documenta explícitamente "resistencia institucional" y "escasa inversión" como barreras a la adopción tecnológica hospitalaria en la región | 
| S2 | Blog USIL, "La inoperatividad de los equipos médicos..." (2026)  | Artículo periodístico-técnico con entrevista a experto | Incluir | Explica que la inoperatividad se debe a deficiencias de gestión técnica, no solo de presupuesto; testimonio de director de carrera de Ing. Biomédica |
| S3 | Gestión.pe, "Biomedicina en el Perú..." (2023)  | Nota periodística con entrevista a docente UPCH | Incluir | Confirma, desde la propia UPCH, la brecha institucional en el desarrollo de la ingeniería clínica en el país |
| S4 | DIGEMID/CENAFyT, Boletín de Farmacovigilancia y Tecnovigilancia (dic. 2024 / jun. 2025)  | Fuente oficial (boletín regulatorio) | Incluir | Es el propio regulador reconociendo retos pendientes tras 20 años del sistema; da cifras de notificaciones SIADM 2016-2024 |
| S5 | "Incidentes adversos asociados a dispositivos médicos en el Hospital María Auxiliadora, 2024" (ALICIA-CONCYTEC)  | Estudio/tesis de repositorio académico |Incluir | Evidencia empírica a nivel de un hospital público peruano, dentro del rango de 6 años |
| S6 | "Notificación de probabilidad de incidentes adversos a dispositivos médicos, INSN San Borja, 2020-2022" (ALICIA-CONCYTEC) | Estudio/tesis de repositorio académico | Incluir como complementaria | Segundo caso hospitalario peruano; permite comparar dos establecimientos distintos |
| S7 | INEI, "Informe Técnico: Evolución de los Indicadores de Pobreza Multidimensional, 2016-2025" | Dato oficial (INEI/MIDIS) | Incluir | Fuente base proporcionada; contextualiza la brecha de salud a nivel nacional |
| S8 | Manual de evaluación de tecnologías sanitarias, IETS Colombia | Manual institucional | Excluir de la matriz de evidencia | Corresponde a otro país (Colombia); útil solo como referencia comparativa opcional |
---

## Hoja de trabajo 3
## 📷 **Matriz de evidencia**

| ID / Autor | Referencia y enlace | Método y contexto | Hallazgo + limitación | Implicación para el reto ODS |
|---|---|---|---|---|
| E1 · Mauricio et al. | D. Mauricio *et al.*, "Electronic Health Record Interoperability System in Peru Using Blockchain," *Int. J. Online Biomed. Eng. (iJOE)*, vol. 20, no. 3, pp. 136–153, 2024. doi: 10.3991/ijoe.v20i03.44507 | Diseño de arquitectura + prototipo web basado en blockchain y HL7 FHIR para intercambiar HCE entre sistemas heterogéneos peruanos, 2024 | Confirma que en Perú no existe un sistema de HCE integrado que se comparta automáticamente entre establecimientos, lo que eleva costos por exámenes duplicados y tiempo de gestión. Limitación: el prototipo no está desplegado a escala nacional real | Valida técnicamente que la brecha sigue vigente y que el estándar de referencia para resolverla es HL7 FHIR |
| E2 · Rev. TecnoHumanismo (Lima) | "Plataforma Digital e Historias Clínicas Electrónicas desde la perspectiva de vinculación con el Sistema Nacional de Salud, Lima 2022," *TecnoHumanismo*, vol. 2, no. 2, 2022 | Revisión sistemática descriptiva (diagrama PRISMA) sobre plataformas digitales y HCE en el Sistema Nacional de Salud, Lima, 2022 | Señala que solo ~52.6% de los países de la OPS cuenta con un sistema nacional consolidado y que el índice de desarrollo electrónico regional avanzó de 0.4 (2010) a 0.7 (2020). Limitación: es una síntesis de literatura, no mide directamente establecimientos peruanos | Sitúa a Perú dentro de una brecha regional de desarrollo de salud digital, no solo un problema local aislado |
| E3 · Asociación Médica Peruana | Asociación Médica Peruana, "Fragmentación informática en salud y el Plan Nacional de Telesalud," amp.pe, 2026 | Artículo de análisis de política sectorial de salud digital, 2026 | Detalla consecuencias concretas: duplicidad de registros, errores de digitación, pérdida de atenciones/reembolsos, imposibilidad de portabilidad de la HC del paciente (ej.: atenciones en la plataforma Teleatiendo que no aparecen en la HCE). Limitación: es un artículo de opinión/análisis, sin datos primarios cuantitativos | Aporta ejemplos concretos y actuales para justificar por qué la fragmentación afecta la continuidad de atención (meta 3.8) |
| E4 · OPS/OMS | Organización Panamericana de la Salud, "Transformación digital: Perú valida interoperabilidad de historias clínicas electrónicas," paho.org, 20 jun. 2025 | Nota institucional sobre la "Conectatón IPS Perú 2025" (MINSA, con apoyo de BID y OPS), participación de 36 entidades públicas/privadas/mixtas | Confirma que recién en 2025 se valida técnicamente el intercambio de historias clínicas bajo el RENHICE; es decir, la interoperabilidad plena aún no opera a nivel nacional. Limitación: nota de prensa institucional, no mide cobertura poblacional real | Da una fecha de referencia concreta (2025) para medir avances futuros del proyecto |
| E5 · Asociación Médica Peruana | Asociación Médica Peruana, "Conectatón, interoperabilidad e Historia Clínica Electrónica," amp.pe, 2026 | Artículo técnico-normativo sobre los estándares HL7/FHIR adoptados por el MINSA | Confirma que "el sector salud no cuenta con una línea de base de interoperabilidad plena entre todos los establecimientos", que se encuentra en fase de preparación, estandarización y acreditación. Limitación: no ofrece una métrica numérica de cobertura | Sustenta que el indicador 3.8.1 aún no puede calcularse de forma completa por falta de datos interoperables → vacío de datos identificado |
| E6 · INEI (dato oficial) | Instituto Nacional de Estadística e Informática (INEI), "Informe Técnico: Evolución de los Indicadores de Pobreza Multidimensional, 2016-2025," gob.pe, 2026 | Informe técnico oficial que mide la pobreza multidimensional peruana en 8 dimensiones (salud, educación, vivienda, servicios básicos, empleo y previsión social, conectividad, seguridad, energía), según D.S. N.° 014-2024-MIDIS | Es la fuente oficial y más reciente sobre magnitud de la brecha de acceso a salud y conectividad en Perú. Limitación: mide privación de *acceso* a servicios en general, no mide directamente la fragmentación de los sistemas de información clínica (variable más técnica de este reto) | Da la "evidencia local/contextual" de la Ficha ODS: conecta la brecha tecnológica con la pobreza multidimensional medida oficialmente |
| E7 · RPP / índice U. de Lima (opcional) | RPP Noticias, "Pobreza multidimensional: 10.8 millones de peruanos carecen de servicios de salud, educación, vivienda y conectividad," rpp.pe, 29 ene. 2026 | Reportaje que difunde un índice elaborado por la Universidad de Lima (mientras el índice oficial INEI se terminaba de definir) | El 32% de la población peruana (10.8 millones de personas) enfrenta pobreza multidimensional por carencia conjunta en salud, educación, vivienda y conectividad. Limitación: es un índice académico no oficial, útil solo como aproximación | Cuantifica a la población potencialmente afectada por la brecha combinada salud + conectividad, útil para el párrafo 1 y 2 del brief |


### Síntesis de evidencia
| Coincidencias | Contradicciones / límites | Vacíos prioritarios |
|---|---|---|
| Todas las fuentes técnicas y normativas (E1, E3, E4, E5) coinciden en que el sistema de salud peruano está fragmentado en subsectores (MINSA, EsSalud, sanidades FF.AA./FF.PP., privado) sin una historia clínica única, y que el estándar adoptado para resolverlo es HL7 FHIR | Las fuentes institucionales (E4, E5) presentan 2025 como un "hito" de validación técnica, pero ninguna ofrece todavía una métrica de cobertura poblacional real (% de establecimientos interoperando). La solución técnica más concreta (E1, blockchain + FHIR) sigue siendo un prototipo, no una implementación nacional | (1) No hay un dato público que cruce el mapa de pobreza multidimensional (INEI, E6) con el mapa real de establecimientos que ya interoperan vía RENHICE; (2) falta evidencia cuantitativa reciente sobre costo/tiempo perdido por duplicidad de historias clínicas a nivel nacional; (3) no existe todavía una línea base numérica del indicador 3.8.1 asociada específicamente a la fragmentación informática |

## Hoja de trabajo 4

### Decisión ODS y formulación del reto
| Secuencia obligatoria: brecha y afectados → meta cuyo resultado cambiaría → indicador global → medida próxima del proyecto. El indicador ODS no es la misma cosa que una métrica técnica del prototipo. |
| --- |

### Ficha ODS
| CAMPO | RESPUESTA DEL EQUIPO | FUENTE / ENLACE |
| --- | --- | --- | 
| Reto respaldado (sin solución) | [Escriba aquí] | [Fuente(s) que lo sostienen]
| ODS principal | [Número y nombre] | [ONU] |
| Meta específica | [Código y texto pertinente] | [ONU / CEPAL] |
| Indicador global | [Código y nombre] | [ONU / INEI] |
| Evidencia local o contextual | [Dato que conecta la brecha con la meta] | [INEI / fuente oficial / artículo] |
| Medida próxima del proyecto | [Dato alcanzable: tiempo, costo, error, cobertura, acceso, merma, etc.] | [Cómo se observaría] | 
| ODS secundario (opcional) | [Solo si existe relación demostrable] | [Fuente] |
| Dato faltante | [Qué falta medir o validar] | [Plan para obtenerlo] |

### Justificación de la decisión
| PREGUNTA DE CONTROL | RESPUESTA |
| --- | --- | 
| ¿Qué resultado de la meta cambiaría si el reto se comprendiera o redujera? | [Escriba aquí] |
| ¿Qué evidencia demuestra la relación y evita elegir el ODS solo por afinidad con la carrera? | [Escriba aquí] |
| ¿Qué no puede afirmar todavía el equipo? | [Escriba aquí] |

### Fórmula para el reto inicial
| **Complete sin presuponer una solución:** [Actor o sistema] enfrenta [brecha verificable] en [contexto], lo que produce [consecuencia respaldada]. El equipo necesita comprender [causa o vacío] para contribuir a la meta [código], observando inicialmente [medida próxima]. |
| --- |

## Hoja de trabajo 5
## 📜 **Brief de cinco párrafos**

| PÁRRAFO / RESPONSABLE | FUNCIÓN Y CONTENIDO OBLIGATORIO | TEXTO |
| --- | --- | --- |
| 1 • [Nombre] | [Contexto y magnitud: presente la brecha, un dato verificable, lugar/periodo y población o sistema afectado. Conecte el problema con el cambio que importa.] | [Redacte aquí 120–160 palabras con cita(s) IEEE] |
| 2 • [Nombre] | [Afectados y consecuencias: explique quién o qué proceso resulta afectado, cómo se manifiesta y por qué merece atención. Relacione la consecuencia con la meta ODS candidata.] | [Redacte aquí 120–160 palabras con cita(s) IEEE] | 
| 3 • [Nombre] | [Causas o factores: sintetice evidencia sobre causas, condiciones o mecanismos. Distinga dato de interpretación y reconozca límites del contexto.] | [Redacte aquí 120–160 palabras con cita(s) IEEE] | 
| 4 • [Nombre] | [Respuesta existente y vacío: describa qué se ha intentado o cómo se mide hoy, sin vender una solución. Señale limitaciones y el vacío que el equipo debe comprender.] | [Redacte aquí 120–160 palabras con cita(s) IEEE]] | 
| 5 • [Nombre] | [Síntesis y reto: justifique ODS, meta e indicador;  diferencie la medida próxima del indicador global y cierre con el reto inicial respaldado y el dato faltante.] | [Redacte aquí 120–160 palabras con cita(s) IEEE]] |
