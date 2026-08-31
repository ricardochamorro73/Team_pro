# Evidencia y ODS — Fragmentación e interoperabilidad de la información en salud (Perú)

> Ingeniería Biomédica · UPCH · Semana 2
> Reto trabajado con evidencia real (INEI + fuentes técnicas/normativas de salud digital). Los campos marcados como `[completar]` dependen de datos propios del equipo (nombres, fecha exacta, resultados de tu propia corrida de búsqueda).

---

## Hoja de trabajo 1

### Pregunta y términos

| Equipo | Carrera | Reto o tema inicial | ODS candidato |
|---|---|---|---|
| `[N.º / nombre del equipo]` | Ingeniería Biomédica | Fragmentación e interoperabilidad incompleta de la información clínica entre los subsistemas de salud del Perú (MINSA, EsSalud, sanidades FF.AA./FF.PP., sector privado) | ODS 3 — Salud y bienestar (puede ajustarse tras revisar más evidencia) |

### Pregunta de evidencia

> ¿Qué evidencia describe **la fragmentación de los sistemas de información clínica** en **los establecimientos de salud del Perú** dentro de **el Sistema Nacional de Salud**, cuáles son sus causas o consecuencias y qué cambio se relaciona con **la interoperabilidad de la historia clínica electrónica (HCE)**?

### Tabla de conceptos y términos

| Bloque | Español | Inglés / sinónimos | Término controlado o de índice | Aporte a la consulta |
|---|---|---|---|---|
| Actor / sistema | Sistema de historia clínica electrónica (HCE); establecimientos de salud (MINSA, EsSalud, privados) | Electronic Health Record (EHR); Health Information System (HIS) | MeSH: *Electronic Health Records*; IEEE/INSPEC keyword: *Health information systems* | Define el objeto tecnológico central a buscar |
| Brecha / fenómeno | Fragmentación e interoperabilidad incompleta de la información clínica | Data fragmentation; Health information interoperability; Health Information Exchange (HIE) | MeSH: *Health Information Interoperability*; IEEE keyword: *Interoperability*, *HL7 FHIR* | Es el núcleo del problema; sin este término la búsqueda es demasiado amplia |
| Contexto | Sistema de salud peruano segmentado en subsectores (MINSA, EsSalud, FF.AA./FF.PP., privado) | Peru; fragmented/segmented health system; low- and middle-income country (LMIC) | MeSH: *Peru* [Geographic]; Author keyword: *Latin America* | Delimita geográfica e institucionalmente la búsqueda |
| Consecuencia | Duplicidad de historias clínicas, pérdida de continuidad de atención, errores de transcripción, sobrecostos | Duplicate medical records; continuity of care; medical errors; healthcare costs | MeSH: *Continuity of Patient Care*; *Medical Errors* | Acota el impacto y a los afectados que se buscan documentar |

### Consultas exactas que se ejecutarán

| Base | Consulta completa | Filtros planificados | Responsable |
|---|---|---|---|
| PubMed / MEDLINE | `("electronic health records"[MeSH] OR "health information interoperability") AND (Peru) AND (fragmentation OR "health information exchange")` | Años 2019–2026; artículos y revisiones; texto en inglés/español | `[Nombre]` |
| IEEE Xplore | `("interoperability" AND "electronic health record" AND "Peru")` | Años 2019–2026; conference papers y journals; tema "Health informatics" | `[Nombre]` |

---

## Hoja de trabajo 2

### 🔍 Registro de búsqueda y triage

> Estas 5 búsquedas ya las corrí yo (PubMed e IEEE Xplore vía buscadores públicos, SciELO/Google Scholar directo). Los conteos son reales, no inventados — con acceso institucional Scopus/IEEE Xplore completo es probable que el número de "revisados" suba.

| Fecha | Base | Consulta exacta | Filtros | Revisados / incluidos | Resp. |
|---|---|---|---|---|---|
| 30/08/2026 | Búsqueda exploratoria (prensa especializada + repositorios abiertos) | `interoperabilidad historia clínica electrónica Perú fragmentación` | Últimos 6 años (2020–2026) | 15 / 7 | `[Nombre]` |
| 30/08/2026 | PubMed | `("electronic health records"[MeSH] OR "health information interoperability") AND (Peru) AND (fragmentation OR "health information exchange")` | 2019–2026 | 9 / 0 — no aparecen artículos Perú-específicos indexados en PubMed; los resultados son de interoperabilidad de HCE en general (EE.UU., Europa). El estudio peruano más relevante (Mauricio et al., 2024) está indexado en Scopus, no en PubMed | `[Nombre]` |
| 30/08/2026 | IEEE Xplore | `("interoperability" AND "electronic health record" AND "Peru")` | 2019–2026 | 6 / 1 — confirma el mismo estudio ya usado en la matriz (Mauricio et al., 2024, iJOE, con arquitectura basada en HL7 FHIR y blockchain) | `[Nombre]` |
| 30/08/2026 | Scopus | `TITLE-ABS-KEY(interoperability AND "electronic health record" AND Peru)` | 2019–2026 | Sin acceso institucional a Scopus desde aquí — pendiente de correr con tu cuenta UPCH; el estudio de Mauricio et al. (2024) sí está indexado ahí | `[Nombre]` |
| 30/08/2026 | SciELO / Google Scholar | `interoperabilidad salud digital Perú historia clínica` | 2019–2026, solo Perú/LatAm | 7 / 1 — confirma la revisión de TecnoHumanismo (Lima, 2022) ya incluida en la matriz | `[Nombre]` |

### 🧪 Triage de fuentes candidatas

| ID | Título corto / año | Tipo de fuente | Decisión | Justificación |
|---|---|---|---|---|
| S1 | Mauricio et al., "EHR Interoperability System in Peru Using Blockchain" (2024) | Artículo — revista indexada (Scopus, biomédica) | Incluir | Es el estudio técnico más directo: confirma que Perú no tiene HCE integrada e interoperable y propone arquitectura con HL7 FHIR |
| S2 | "Plataforma Digital e Historias Clínicas Electrónicas... Sistema Nacional de Salud, Lima 2022" | Revisión sistemática (PRISMA), revista peruana | Incluir | Perú-específico, dentro de 6 años, buscó en IEEE Digital Library/Scopus/SciELO |
| S3 | Asociación Médica Peruana, "Fragmentación informática en salud y el Plan Nacional de Telesalud" (2026) | Artículo de análisis/opinión técnica | Incluir | Da ejemplos concretos y recientes del efecto de la fragmentación (duplicidad, pérdida de reembolsos, caso Teleatiendo) |
| S4 | OPS/OMS, "Perú valida interoperabilidad de historias clínicas electrónicas" (jun. 2025) | Nota institucional oficial (OPS + MINSA + BID) | Incluir | Fuente oficial que fecha el estado de avance real (2025) de la Conectatón/RENHICE |
| S5 | Asociación Médica Peruana, "Conectatón, interoperabilidad e Historia Clínica Electrónica" (2026) | Artículo técnico-normativo | Incluir | Explica los estándares HL7/FHIR adoptados y confirma que no existe todavía línea de base de interoperabilidad plena |
| S6 | INEI, "Informe Técnico: Evolución de los Indicadores de Pobreza Multidimensional, 2016-2025" | Dato oficial (INEI/MIDIS) | Incluir | Es la fuente que diste como punto de partida; mide 8 dimensiones oficiales de pobreza, incluida salud y conectividad |
| S7 | RPP / índice Universidad de Lima, "10.8 millones de peruanos carecen de salud, educación, vivienda y conectividad" (ene. 2026) | Reportaje con dato de índice académico | Incluir (como evidencia complementaria) | Cuantifica cuánta población está afectada por la brecha combinada de salud + conectividad |
| S8 | Rojas Mezarina et al., "Registro Nacional de Historias Clínicas Electrónicas en Perú" (2015) | Artículo — Rev. Peruana de Medicina Experimental y Salud Pública | Excluir | Antigüedad mayor a 6 años (2015); solo útil como antecedente histórico del RENHICE, no como evidencia vigente |
| S9 | Estudio cualitativo sobre uso de HCE en médicos, Buenos Aires (2019–2020) | Artículo académico | Excluir | Ámbito geográfico distinto (Argentina), no Perú; se prioriza evidencia local |

---

## Hoja de trabajo 3

### 📸 Matriz de evidencia

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

---

## Hoja de trabajo 4

### Decisión ODS y formulación del reto

### Ficha ODS

| Campo | Respuesta del equipo | Fuente / enlace |
|---|---|---|
| Reto respaldado (sin solución) | Los establecimientos de salud del sistema peruano (MINSA, EsSalud, sanidades FF.AA./FF.PP. y sector privado) mantienen sistemas de información clínica fragmentados y no interoperables, lo que impide una visión única del paciente y afecta la continuidad de su atención | E1, E3, E4, E5 |
| ODS principal | ODS 3 — Salud y bienestar | ONU |
| Meta específica | Meta 3.8 — "Lograr la cobertura sanitaria universal, incluida la protección contra los riesgos financieros, el acceso a servicios de salud esenciales de calidad y el acceso a medicamentos y vacunas inocuos, eficaces, asequibles y de calidad para todos" | ONU / OPS |
| Indicador global | 3.8.1 — Cobertura de los servicios de salud esenciales | ONU |
| Evidencia local o contextual | El 32% de la población peruana (10.8 millones de personas) enfrenta pobreza multidimensional por carencias conjuntas en salud, educación, vivienda y conectividad; el informe oficial INEI 2016-2025 mide estas 8 dimensiones a nivel nacional | E6, E7 |
| Medida próxima del proyecto | Propuesta a evaluar por el equipo, p. ej.: *porcentaje de historias clínicas de un establecimiento piloto que logran exportarse en formato HL7 FHIR válido*, o *tiempo promedio ahorrado al evitar la repetición de exámenes en una consulta de referencia* — `[el equipo debe elegir y justificar una]` | Cómo se observaría: registro de exportaciones exitosas / tiempo de atención en el prototipo |
| ODS secundario (opcional) | ODS 17 — Alianzas para lograr los objetivos, meta 17.18 (mejorar el apoyo a la creación de capacidad... para aumentar la disponibilidad de datos oportunos, fiables y de alta calidad) | ONU |
| Dato faltante | Porcentaje real de establecimientos de salud (especialmente rurales o en zonas de pobreza multidimensional) con HCE interoperable vía RENHICE; costo/tiempo perdido por duplicidad a nivel nacional | Plan: solicitar datos abiertos a MINSA-OGTI/RENHICE o a SUSALUD, o levantar una mini-encuesta a establecimientos piloto |

### Justificación de la decisión

| Pregunta de control | Respuesta |
|---|---|
| ¿Qué resultado de la meta cambiaría si el reto se comprendiera o redujera? | Mejoraría la cobertura efectiva de servicios de salud esenciales (indicador 3.8.1), porque los pacientes recibirían atención continua sin repetir exámenes ni perder información al cambiar de establecimiento |
| ¿Qué evidencia demuestra la relación y evita elegir el ODS solo por afinidad con la carrera? | Los datos oficiales de INEI (E6) y el índice de pobreza multidimensional (E7) muestran que la falta de acceso a salud y conectividad afecta a millones de peruanos, y las fuentes técnicas (E1, E4, E5) confirman que la fragmentación de las HCE es una causa estructural vigente de esa brecha, no solo un tema técnico aislado |
| ¿Qué no puede afirmar todavía el equipo? | Que la interoperabilidad por sí sola reduzca la pobreza multidimensional, ni cuál es el porcentaje real de establecimientos que hoy interoperan fuera del piloto de la Conectatón |

### Fórmula para el reto inicial

> Los establecimientos de salud del sistema peruano (MINSA, EsSalud, sanidades FF.AA./FF.PP. y sector privado) enfrentan una interoperabilidad incompleta de sus sistemas de historia clínica electrónica en el contexto del Sistema Nacional de Salud, lo que produce duplicidad de registros, pérdida de continuidad de atención y sobrecostos por exámenes repetidos. El equipo necesita comprender las causas técnicas y normativas de esta fragmentación para contribuir a la meta 3.8, observando inicialmente el porcentaje de historias clínicas que logran intercambiarse exitosamente bajo el estándar HL7 FHIR en un establecimiento piloto.

---

## Hoja de trabajo 5

### 📝 Brief de cinco párrafos

*(Borrador redactado en 120–160 palabras por párrafo, con citas IEEE numeradas según la lista de referencias al final. Ajusta el nombre del responsable de cada párrafo.)*

**Párrafo 1 · Contexto y magnitud** — `[Nombre]`
En el Perú, la atención de salud está repartida entre subsectores que no comparten una sola historia clínica: MINSA, EsSalud, las sanidades de las Fuerzas Armadas y Policiales, y el sector privado [1]. Esta segmentación institucional es la raíz de la fragmentación informática que hoy enfrenta el sistema. A nivel país, el problema no es marginal: el índice de pobreza multidimensional del Instituto Nacional de Estadística e Informática mide ocho dimensiones —entre ellas salud y conectividad— y, según una aproximación reciente basada en ese enfoque, el 32% de los peruanos, unos 10.8 millones de personas, carece de manera conjunta de servicios adecuados de salud, educación, vivienda y conectividad [7]. Esa brecha de conectividad es, precisamente, la que dificulta que la información clínica viaje con el paciente entre establecimientos, y conecta el problema tecnológico con un cambio de fondo: la cobertura sanitaria universal.

**Párrafo 2 · Afectados y consecuencias** — `[Nombre]`
Los principales afectados son los pacientes que se atienden en más de un establecimiento a lo largo del tiempo, y el personal de salud que los atiende sin acceso a su historial completo. Cuando un paciente cambia de sede o de subsistema, su información no lo acompaña automáticamente, lo que obliga a repetir exámenes, aumenta la carga administrativa del personal y genera errores de transcripción [3]. Un ejemplo documentado es el de pacientes atendidos por plataformas de teleconsulta cuya atención no queda registrada en la historia clínica electrónica del establecimiento físico, rompiendo la continuidad del cuidado [3]. Estas consecuencias se relacionan directamente con la meta 3.8, ya que la cobertura sanitaria universal no solo depende de que exista un servicio, sino de que la atención sea continua, segura y no se pierda entre un sistema y otro.

**Párrafo 3 · Causas o factores** — `[Nombre]`
La causa técnica central es la ausencia de un estándar único y obligatorio de intercambio de datos clínicos entre subsectores. El Ministerio de Salud ha adoptado progresivamente el estándar internacional HL7 FHIR como base de la interoperabilidad, pero su implementación aún está en fase de estandarización y acreditación, sin una línea de base de cobertura plena entre todos los establecimientos [5]. Un estudio técnico reciente propuso incluso una arquitectura basada en blockchain para homologar formatos heterogéneos hacia HL7 FHIR, justamente porque hoy "no existe un sistema de historia clínica electrónica integrado que pueda compartirse automáticamente" entre establecimientos peruanos [1]. A esto se suma un factor regional: el desarrollo de salud electrónica en América Latina avanzó de un índice de 0.4 a 0.7 entre 2010 y 2020, pero solo alrededor de la mitad de los países de la región cuenta con un sistema nacional consolidado [2].

**Párrafo 4 · Respuesta existente y vacío** — `[Nombre]`
Como respuesta, el MINSA impulsa el Registro Nacional de Historias Clínicas Electrónicas (RENHICE) y en 2025 realizó la "Conectatón IPS Perú", un ejercicio técnico con apoyo de la OPS y el BID en el que 36 entidades públicas, privadas y mixtas validaron por primera vez su capacidad de intercambiar información clínica bajo estándares internacionales [4]. Sin embargo, esta validación es todavía un ejercicio piloto, no una operación nacional plena: no existe aún una métrica pública sobre qué porcentaje de establecimientos —sobre todo en zonas rurales o de mayor pobreza multidimensional— efectivamente interoperan en el día a día [4], [5]. Ese es el vacío central que el equipo necesita comprender antes de proponer cualquier solución: se sabe que el problema existe y que hay un camino normativo trazado, pero falta el dato que muestre cuánto de ese camino ya se recorrió en la práctica.

**Párrafo 5 · Síntesis y reto** — `[Nombre]`
En conjunto, la evidencia respalda trabajar sobre el ODS 3, meta 3.8 (cobertura sanitaria universal), medida por el indicador 3.8.1 de cobertura de servicios de salud esenciales [ONU]. La medida próxima del proyecto no debe confundirse con este indicador global: mientras 3.8.1 mide cobertura poblacional agregada, el equipo puede observar inicialmente algo más concreto y alcanzable, como el porcentaje de historias clínicas de un establecimiento piloto que logran exportarse correctamente en formato HL7 FHIR. El reto inicial respaldado, sin proponer todavía una solución, es que los establecimientos del sistema de salud peruano enfrentan una interoperabilidad incompleta de sus historias clínicas electrónicas, lo que afecta la continuidad de atención y contribuye a la brecha de salud que hoy sufren millones de peruanos [6], [7]. El dato que aún falta —y que el equipo debe conseguir— es el porcentaje real de establecimientos, especialmente los ubicados en zonas de pobreza multidimensional, que hoy interoperan efectivamente fuera del piloto de la Conectatón.

---

## Referencias (formato IEEE)

[1] D. Mauricio, P. C. Llanos-Colchado, L. S. Cutipa-Salazar, P. Castañeda, R. Chuquimbalqui-Maslucán, L. Rojas-Mezarina, and J. L. Castillo-Sequera, "Electronic Health Record Interoperability System in Peru Using Blockchain," *International Journal of Online and Biomedical Engineering (iJOE)*, vol. 20, no. 3, pp. 136–153, 2024. doi: 10.3991/ijoe.v20i03.44507.

[2] "Plataforma Digital e Historias Clínicas Electrónicas desde la perspectiva de vinculación con el Sistema Nacional de Salud, Lima 2022," *TecnoHumanismo. Revista Científica*, vol. 2, no. 2, 2022. *(verificar autoría exacta en la fuente original antes de citar en el trabajo final)*.

[3] Asociación Médica Peruana, "Fragmentación informática en salud y el Plan Nacional de Telesalud," *amp.pe*, 2026. [En línea]. Disponible: https://amp.pe/fragmentacion-informatica-en-salud-y-el-plan-nacional-de-telesalud/

[4] Organización Panamericana de la Salud, "Transformación digital: Perú valida interoperabilidad de historias clínicas electrónicas," *paho.org*, 20 jun. 2025. [En línea]. Disponible: https://www.paho.org/es/noticias/20-6-2025-transformacion-digital-peru-valida-interoperabilidad-historias-clinicas

[5] Asociación Médica Peruana, "Conectatón, interoperabilidad e Historia Clínica Electrónica," *amp.pe*, 2026. [En línea]. Disponible: https://amp.pe/conectaton-interoperabilidad-e-historia-clinica-electronica/

[6] Instituto Nacional de Estadística e Informática (INEI), "Informe Técnico: Evolución de los Indicadores de Pobreza Multidimensional, 2016-2025," Lima, Perú, 2026. [En línea]. Disponible: https://cdn.www.gob.pe/uploads/document/file/10407775/8445753-informe-tecnico-pobreza-multidimensional-2016-2025.pdf

[7] RPP Noticias, "Pobreza multidimensional: 10.8 millones de peruanos carecen de servicios de salud, educación, vivienda y conectividad," *rpp.pe*, 29 ene. 2026. [En línea]. Disponible: https://rpp.pe/economia/economia/pobreza-multidimensional-108-millones-de-peruanos-carecen-de-servicios-de-salud-educacion-vivienda-y-conectividad-noticia-1673643

---

## Notas para completar antes de entregar

- [ ] Poner nombre/número real del equipo y responsables en cada tabla.
- [ ] Correr tú mismo las consultas de PubMed, IEEE Xplore y Scopus (Hoja 2) con tu acceso institucional UPCH y anotar los resultados reales.
- [ ] Verificar la autoría exacta de la referencia [2] (TecnoHumanismo) antes de usarla formalmente.
- [ ] Elegir y justificar la "medida próxima del proyecto" (Hoja 4) según lo que el equipo pueda medir en la práctica.
- [ ] Si el docente pide el PDF exacto del INEI como anexo, descárgalo directamente desde el enlace oficial (el sitio bloquea la descarga automática, así que hazlo manualmente desde el navegador).
