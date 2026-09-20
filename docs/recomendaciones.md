# Recomendaciones Estratégicas — Reto 7
## Traducción de hallazgos a decisiones empresariales

---

**Curso:** Business Intelligence y Big Data — Curso 6  
**Reto:** 7 — Análisis de Datos No Estructurados y Redes Sociales  
**Analista:** Judit Giravent
**Fecha:** Septiembre 2026
**Documento complementario a:** `informe_analisis.md`

---

## Resumen ejecutivo de recomendaciones

Basado en el análisis de **100,000 tweets sobre IA (marzo 2023)**, este documento presenta **17 recomendaciones accionables** organizadas en 5 áreas estratégicas. Las recomendaciones emanan directamente de los hallazgos empíricos del análisis y están priorizadas por **impacto esperado × facilidad de implementación**.

### Las 5 conclusiones accionables principales

| # | Recomendación clave | Área | Prioridad |
|---|---------------------|------|-----------|
| 1 | **Aprovechar la "ventana positiva"** — el sentimiento favorable es una oportunidad de 6-12 meses | Marketing | 🔥 Crítica |
| 2 | **Co-ocurrir con ChatGPT** para ganar visibilidad en el discurso IA | Marketing | 🔥 Crítica |
| 3 | **Evitar el ruido cripto-IA** si no es el core del negocio | Marketing | ⚡ Alta |
| 4 | **Atender la demanda de herramientas prácticas** (escritura, código, PDFs) | Producto | 🔥 Crítica |
| 5 | **Posicionarse frente a Google Bard** como alternativa complementaria | Producto | ⚡ Alta |

---

## Contexto: por qué estas recomendaciones y no otras

Tres hallazgos del análisis condicionan **qué tipo de decisiones** son relevantes:

1. **El sentimiento positivo es dominante (53.26%)** con engagement reforzado. Esto significa que **la IA no está en crisis reputacional** — la ventana para posicionar productos positivos está abierta.

2. **La red de entidades se organiza en 4 comunidades con ChatGPT como hub absoluto (grado 2,344)**. Esto significa que **la visibilidad pasa por co-ocurrir con ChatGPT** — un producto que no aparezca mencionado junto a ChatGPT quedará invisible en el discurso.

3. **La comunidad cripto-IA es un nicho significativo (~11,300 tweets)**. Esto significa que existe una **convergencia real** entre IA generativa y generación de contenido digital, que puede ser una oportunidad (o un ruido) según el posicionamiento de cada empresa.

Estas tres observaciones guían todas las recomendaciones siguientes.

---

## Área 1 — Marketing y Comunicación

### Recomendación 1.1: Aprovechar la ventana positiva antes del ciclo negativo

**Hallazgo empírico:**
- 53.26% de tweets positivos
- 16.06% negativos
- Compound medio +0.2174
- Los tweets positivos generan **9.49 likes** vs. 7.23 de los negativos (+31%)

**Hipótesis estratégica:**  
En marzo 2023, la IA está en **fase de adopción temprana optimista**. Históricamente, los ciclos tecnológicos pasan por: entusiasmo → expectativas infladas → desilusión → adopción productiva. **La fase actual está en "entusiasmo"**, con 6-12 meses antes del previsible ciclo de escrutinio crítico.

**Acción concreta:**
1. **Lanzar campañas de posicionamiento positivo** durante los próximos 2 trimestres.
2. **Construir activos de marca** (casos de éxito, testimonios, demos) que sobrevivan al cambio de ciclo.
3. **Preparar un plan de contingencia** para cuando la narrativa pública cambie (probablemente por un incidente ético, una regulación o un fallo público).

**KPI:** Share of voice positivo en Twitter/X  
**Target:** ≥ 15% de crecimiento en 6 meses

---

### Recomendación 1.2: Co-ocurrir con ChatGPT para ganar visibilidad

**Hallazgo empírico:**
- `gpt` tiene grado ponderado 2,344 (4.5× el siguiente)
- ChatGPT aparece en las 4 comunidades detectadas
- 33,279 menciones de `gpt` frente a 1,389 de Google

**Hipótesis estratégica:**  
El algoritmo de Twitter/X y el discurso público **premian los tweets que mencionan ChatGPT**, porque es el tema más discutido. Una empresa que no co-ocurra con ChatGPT quedará fuera del alcance orgánico.

**Acción concreta:**
1. **Crear contenido que mencione explícitamente ChatGPT** (integraciones, comparativas, casos de uso conjunto).
2. **No competir frontalmente** con ChatGPT en el discurso — **complementarlo**.
3. **Ejemplos:**
   - ❌ Mal: "Nuestra IA es mejor que ChatGPT"
   - ✅ Bien: "Nuestra herramienta aprovecha ChatGPT para hacer X"
4. **Publicar 2-3 tweets semanales con mención ChatGPT** en el contenido orgánico.

**KPI:** Porcentaje de tweets propios que mencionan ChatGPT  
**Target:** 40-60% del contenido sobre IA

---

### Recomendación 1.3: Evitar el ruido cripto-IA si no es el core del negocio

**Hallazgo empírico:**
- Temas 2 y 6 del LDA son puramente cripto/NFT (~11,300 tweets, 12%)
- Comunidad 0 de la red incluye `chatgpt plus premium account` pero no entidades cripto
- Existe una **convergencia temática** pero no una fusión real

**Hipótesis estratégica:**  
La comunidad cripto-IA es **ruidosa pero minoritaria**. Una empresa de IA seria **pierde credibilidad** si su contenido se mezcla con jerga cripto (airdrops, NFTs, tokens).

**Acción concreta:**
1. **Segmentar el contenido:** mantén IA y cripto en canales separados si tu audiencia es mainstream.
2. **Evitar jerga cripto** en comunicaciones corporativas salvo si tu público es ese nicho.
3. **Monitorizar el solapamiento:** si empieza a crecer, reconsiderar (puede ser una tendencia emergente).
4. **Excepción:** si vendes a la comunidad cripto, **duplicar la apuesta** — es un nicho con alta afinidad IA.

**KPI:** Ratio de engagement cripto vs. IA en tu contenido  
**Target:** Mantener < 15% de contenido cripto en canales mainstream

---

### Recomendación 1.4: Explotar la temporada de anuncios (estacionalidad)

**Hallazgo empírico:**
- Corpus concentrado en 16-29 marzo 2023
- Pico máximo: **11,848 tweets en un día** (coincidiendo con anuncios de producto)
- Media diaria: 5,882 tweets

**Hipótesis estratégica:**  
Los picos de volumen **no son aleatorios**: coinciden con hitos de producto (lanzamientos, actualizaciones, eventos). Las marcas que **alinean sus lanzamientos** con estos picos tienen más alcance.

**Acción concreta:**
1. **Mapear el calendario de eventos IA** (Google I/O, OpenAI DevDay, Microsoft Build, etc.).
2. **Planificar lanzamientos 24-48h después** de hitos importantes para "surfear" la ola de atención.
3. **Ejemplo:** si OpenAI anuncia GPT-5, publicar al día siguiente "Cómo [tu producto] aprovecha GPT-5".
4. **Cuidado con saturar:** si coincides exactamente, compites con el gigante; si esperas 24h, quedas fuera del pico.

**KPI:** Alcance medio por tweet en ventana de 48h post-hito  
**Target:** +50% vs. baseline

---

## Área 2 — Producto y Desarrollo

### Recomendación 2.1: Priorizar integraciones con ChatGPT API

**Hallazgo empírico:**
- ChatGPT monopoliza las menciones (33,279 vs. 1,389 de Google)
- El "mercado mental" ya reconoce ChatGPT como categoría
- Los temas 0 y 4 muestran demanda de **uso práctico**: escribir, preguntar, generar

**Hipótesis estratégica:**  
Es **más barato y rápido** construir sobre la API de ChatGPT que entrenar modelos propios. La ventaja competitiva no está en el modelo base (commoditizado) sino en **cómo lo integras** en un caso de uso específico.

**Acción concreta:**
1. **Construir sobre OpenAI API** en lugar de entrenar modelos propios.
2. **Diferenciarse por el workflow**, no por el modelo:
   - Vertical específica (legal, salud, finanzas)
   - Integración con sistemas existentes (CRM, ERP, correo)
   - Experiencia de usuario superior
3. **Coste estimado:** desarrollo 3-6 meses, coste de API variable (uso).

**KPI:** Time-to-market vs. modelos propios  
**Target:** Reducción de 6-12 meses

---

### Recomendación 2.2: Atender la demanda de herramientas prácticas

**Hallazgo empírico:**
- Tema 0 (12,573 tweets): **escritura, generación de contenido, prompts**
- Tema 4 (16,980 tweets): **preguntas, respuestas, acceso a información**
- Tema 5 (19,085 tweets): **código, video, búsqueda**
- Tema 7 (11,926 tweets): **educación, herramientas**

**Hipótesis estratégica:**  
El mercado **no pide "otro ChatGPT"** — pide **soluciones específicas** para casos de uso concretos: escribir mejor, programar más rápido, aprender más eficientemente.

**Acción concreta:**
Priorizar por combinación **demanda × competencia débil**:

| Caso de uso | Demanda (temas LDA) | Competencia | Prioridad |
|-------------|---------------------|-------------|-----------|
| Asistente de escritura profesional | 🔥🔥🔥 (Tema 0) | Alta (Jasper, Copy.ai) | 🟡 Media |
| Generación de código asistida | 🔥🔥 (Tema 5) | Alta (Copilot, Cursor) | 🟡 Media |
| Análisis de documentos (PDFs) | 🔥🔥 (Tema 4) | Media (ChatPDF, AskYourPDF) | 🟢 Alta |
| Educación personalizada | 🔥🔥 (Tema 7) | Baja (Khan Academy, Duolingo) | 🟢 **Muy alta** |
| Workflows verticales (legal, salud) | 🔥 (Tema 1) | Muy baja | 🟢 **Muy alta** |

**Recomendación específica:**  
**Atacar verticales específicas** (legal, salud, inmobiliario) donde la competencia genérica no llega y el valor añadido es alto.

**KPI:** NPS de usuarios en vertical específica  
**Target:** ≥ 50 en los primeros 6 meses

---

### Recomendación 2.3: Posicionarse frente a Google Bard como alternativa complementaria

**Hallazgo empírico:**
- Comunidad 1 (19 nodos): **Google, Microsoft, Bard, Bing**
- Tema 7 (11,926 tweets): **Google, Bard, educación, trabajo**
- Bard aparece como **categoría secundaria** frente a ChatGPT

**Hipótesis estratégica:**  
Google Bard está en **fase de adopción temprana**, con menor volumen pero **mayor afinidad con educación y trabajo** (temas donde Google tiene presencia histórica). Una empresa que se posicione como **complemento a Bard** (no competidor) puede capturar usuarios que Google no atiende.

**Acción concreta:**
1. **Integrar Bard API** además de OpenAI API para dar flexibilidad al usuario.
2. **Posicionar el producto como "agnóstico al modelo"** — usa el mejor para cada tarea.
3. **Target específico:** educación (tema 7), donde Bard tiene tracción.
4. **Ejemplo:** "Nuestra plataforma educativa usa Bard para X y ChatGPT para Y".

**KPI:** Adopción de features multi-modelo  
**Target:** 30% de usuarios activos usan ambos modelos

---

### Recomendación 2.4: Invertir en explicabilidad y ética (antesala de la próxima ola crítica)

**Hallazgo empírico:**
- 16.06% de tweets son negativos (16,062 tweets)
- Los temas negativos giran en torno a **sesgos, decisiones, casos éticos**
- Community 2 (política) y Community 3 (medios) reflejan preocupación pública

**Hipótesis estratégica:**  
La ola de crítica **llegará** (regulación, incidentes, escrutinio mediático). Una empresa que **construya ahora** capacidades de explicabilidad, auditoría y ética tendrá **ventaja competitiva cuando el mercado lo exija**.

**Acción concreta:**
1. **Documentar públicamente cómo funciona el modelo** (no la caja negra completa, pero sí el workflow).
2. **Implementar mecanismos de auditoría** (logs, trazabilidad, versioning).
3. **Publicar informes de sesgo** anuales.
4. **Contratar o asesorar con expertos en ética de IA**.
5. **Ventaja a 2-3 años:** cuando la regulación llegue, será coste cero vs. coste alto para competidores.

**KPI:** Documentación de compliance  
**Target:** 100% del pipeline documentado antes de fin de año

---

## Área 3 — Análisis de Datos y Business Intelligence

### Recomendación 3.1: Industrializar el pipeline NLP

**Hallazgo empírico:**
- El pipeline actual funciona pero está en notebooks
- Tarda ~15-20 minutos de procesamiento
- No es reproducible con un solo comando

**Hipótesis estratégica:**  
Un pipeline industrial **multiplica por 10** la capacidad de análisis. Se puede reutilizar para:
- Otros dominios (finanzas, salud, política)
- Otros idiomas
- Otros periodos

**Acción concreta:**
1. **Mover la lógica de notebooks a scripts** en `src/`:
   - `src/extraccion/extractor.py`
   - `src/preparacion/pipeline_nlp.py`
   - `src/analisis/sentimiento.py`, `ner.py`, `lda.py`, `redes.py`
2. **Parametrizar con `argparse` o `hydra`**:
   ```bash
   python -m src.analisis.sentimiento --input data/raw/tweets.csv --output data/processed/

   Tests unitarios con pytest.

Dockerfile para reproducibilidad total.

KPI: Tiempo de re-análisis completo
Target: < 10 minutos end-to-end con un solo comando

Recomendación 3.2: Automatizar la extracción de entidades con diccionario específico del dominio IA
Hallazgo empírico:

spaCy en_core_web_sm generó ruido: don, doesn, gpt gpt, google s

Estas entidades son falsos positivos por contracciones y posesivos ingleses

Hipótesis estratégica:
Un diccionario específico del dominio (con aliases, acrónimos, productos conocidos) reduciría el ruido en un 80-90%. Además, permitiría clasificar entidades por categoría de negocio (modelo, empresa, producto, investigador).

Acción concreta:

Crear un diccionario curado de entidades IA:

ENTIDADES_IA = {
    "openai": ["OpenAI", "open ai"],
    "chatgpt": ["ChatGPT", "chat gpt", "chat-gpt"],
    "gpt4": ["GPT-4", "gpt4", "gpt 4"],
    "bard": ["Bard", "google bard"],
    "claude": ["Claude", "anthropic claude"],
    # ...
}

Matchear por regex + fuzzy matching (Levenshtein distance ≤ 2).

Combinar con spaCy para capturar entidades no listadas.

Resultado esperado: reducir falsos positivos de ~30% a <5%.

KPI: Precisión de NER manual (muestra de 500 tweets)
Target: ≥ 90%

Recomendación 3.3: Monitorización continua con dashboard
Hallazgo empírico:

El análisis es estático (una foto de marzo 2023)

No hay sistema de alertas

No se puede detectar cambios en tiempo real

Hipótesis estratégica:
Un dashboard semanal de sentimiento y temas permite anticipar crisis y detectar oportunidades antes que la competencia.

Acción concreta:

Setup técnico:

Twitter API (plan Basic o Pro, ~$100-5000/mes según volumen)

Airflow o Prefect para orquestación

Streamlit o Dash para visualización

PostgreSQL o DuckDB para almacenamiento

Métricas a monitorizar:

Sentimiento diario/semanal

Top entidades emergentes

Nuevas comunidades en la red

Alertas si sentimiento cae > 5% en 24h

Coste estimado: $200-800/mes + 1-2 semanas de setup.

KPI: Tiempo de detección de cambio en sentimiento
Target: < 24 horas desde el evento

Recomendación 3.4: Complementar con análisis de interacciones reales
Hallazgo empírico:

La red de co-ocurrencia no refleja interacciones reales

No se analizan retweets, replies ni menciones

No se puede medir influencia social sino proximidad temática

Hipótesis estratégica:
El análisis de interacciones reales (¿quién retuitea a quién? ¿quién menciona a quién?) revela estructuras de influencia que la co-ocurrencia no captura.

Acción concreta:

Extender la extracción para capturar:

retweeted_status (retweets)

in_reply_to_user_id (replies)

entities.user_mentions (menciones)

Construir grafo dirigido:

Nodo = usuario

Arista = interacción

Peso = frecuencia

Métricas adicionales:

PageRank para influencia

HITS para autoridad

Detección de comunidades en grafo dirigido

Resultado esperado: identificar los verdaderos líderes de opinión (no solo las marcas más mencionadas).

KPI: Correlación entre ranking de influencia y métricas tradicionales
Target: Identificar ≥ 10 líderes emergentes no detectados antes

Área 4 — Estrategia Empresarial
Recomendación 4.1: Elegir 1-2 comunidades y dominarlas
Hallazgo empírico:

4 comunidades en la red

ChatGPT domina la comunidad 0

Google-Microsoft dominan la comunidad 1

Política y medios son periféricas

Hipótesis estratégica:
Intentar cubrir todas las comunidades diluye recursos. Mejor elegir 1-2 donde tengas ventaja y dominarlas.

Acción concreta:
Evaluar 3 caminos mutuamente excluyentes:

Camino A: "Alternativa a OpenAI"

Comunidad 1 (Google, Microsoft, Bard)

Requiere: capital, tecnología puntera, marca fuerte

Riesgo: alto, competir contra gigantes

Camino B: "Nicho vertical específico"

Comunidad periférica (educación, legal, salud)

Requiere: expertise de dominio, foco

Riesgo: medio, mercado más pequeño pero menos competido

Camino C: "Herramienta complementaria"

Ecosistema OpenAI/Google

Requiere: agilidad, UX, integración

Riesgo: bajo, dependencia de APIs

Recomendación: Camino B o C según recursos. El Camino A está reservado para quienes tienen >$100M de capital.

KPI: Cuota de mercado en la comunidad elegida
Target: Top 3 en 18 meses

Recomendación 4.2: Invertir en el segmento hispanohablante (mercado desatendido)
Hallazgo empírico:

99.77% de tweets en inglés

Solo 229 tweets en español (0.23%)

La conversación IA en español es prácticamente inexistente en este corpus

Hipótesis estratégica:
El mercado hispanohablante existe (500M+ personas, mercado de $1.5T) pero no participa de la conversación global en inglés. Esto es una oportunidad desatendida para quien se posicione primero.

Acción concreta:

Producir contenido IA en español de calidad (no traducción automática).

Casos de uso locales: legislación LATAM, normativas España, contextos culturales.

Partner con creadores hispanohablantes (YouTube, TikTok, LinkedIn).

Ventaja competitiva: OpenAI, Google y Microsoft tienen productos en inglés; su versión en

español es secundaria.

Riesgo: mercado más pequeño, pero competencia casi nula.

KPI: Presencia en top-of-mind del mercado hispanohablante
Target: Top 5 marcas IA en español en 12 meses

Recomendación 4.3: Construir narrativa positiva pero no ingenua
Hallazgo empírico:

53% positivo, 16% negativo

Los temas negativos giran en torno a ética, sesgos, decisiones, política

El engagement de los negativos no es despreciable (7.23 likes medios)

Hipótesis estratégica:
Una narrativa puramente positiva se percibe como ingenua. Una narrativa positiva pero consciente de los riesgos genera más credibilidad a largo plazo.

Acción concreta:

Comunicación balanceada:

✅ Destacar beneficios concretos

✅ Reconocer limitaciones y desafíos

✅ Mostrar cómo se abordan (ética, sesgos, transparencia)

Framework de mensajes:

70% beneficios y casos de éxito

20% desafíos y cómo los abordamos


0% visión a largo plazo

Evitar:

Optimismo exagerado ("la IA resolverá todo")

Catastrofismo ("la IA nos destruirá")

Ambigüedad (decir nada concreto)

KPI: Índice de confianza de marca (encuestas trimestrales)
Target: ≥ 7/10

Área 5 — Innovación y Futuro
Recomendación 5.1: Monitorizar la emergencia de nuevas comunidades
Hallazgo empírico:

En marzo 2023 hay 4 comunidades claras

La comunidad cripto-IA emergió recientemente (temas 2 y 6)

No hay comunidades emergentes de otras industrias (aún)

Hipótesis estratégica:
Las comunidades emergentes son la antesala de las tendencias. Detectar una comunidad naciente (ej. "IA + salud mental") 3-6 meses antes que la competencia da una ventaja de first-mover decisiva.

Acción concreta:

Dashboard de comunidades actualizado mensualmente.

Alertas automáticas cuando:

Una nueva comunidad > 100 nodos emerge

Una comunidad pequeña crece >50% en 30 días

Aparecen entidades nuevas en top-50

Análisis cualitativo cuando se detecta: ¿es moda pasajera o tendencia estructural?

KPI: Detección temprana de tendencias
Target: 3-6 meses antes que el mainstream

Recomendación 5.2: Invertir en IA generativa multimodal (imagen/video/audio)
Hallazgo empírico:

Tema 0 incluye midjourney (generación de imágenes)

Tema 5 incluye video

El corpus es mayoritariamente texto, pero hay señales multimodales

Hipótesis estratégica:
La próxima ola de IA será multimodal (texto + imagen + video + audio). Las empresas que inviertan ahora en esta tecnología estarán listas cuando el mercado la demande masivamente.

Acción concreta:

Explorar APIs multimodales: DALL-E, Midjourney, Runway, ElevenLabs.

Casos de uso concretos:

Generación de contenido para redes (texto + imagen)

Edición de video asistida por IA

Locución / doblaje automatizado

Timing: empezar con proyectos piloto en 2026, escalar en 2027-2028.

KPI: % de features multimodales en el roadmap
Target: 30% del roadmap para 2027

Recomendación 5.3: Prepararse para la regulación (AI Act europea)
Hallazgo empírico:

Comunidad 2 (política) y 3 (medios) reflejan preocupación

Tema 3 (futuro) incluye powerful, human, time

El discurso negativo se centra en ética y decisiones

Hipótesis estratégica:
La AI Act europea (aprobada en 2024, aplicable progresivamente hasta 2027) va a cambiar las reglas del juego. Las empresas que documenten compliance ahora tendrán ventaja cuando la regulación sea exigible.

Acción concreta:

Clasificar tus sistemas según riesgo (inaceptable, alto, limitado, mínimo).

Implementar:

Registro de decisiones automatizadas

Auditoría de sesgos

Transparencia hacia usuarios

Consentimiento explícito cuando aplique

Nombrar un responsable de compliance IA.

Documentar en un archivo consultable por reguladores.

KPI: % de sistemas documentados según AI Act
Target: 100% antes de 2027


Tabla resumen de priorización
Recomendación	Impacto	Facilidad	Prioridad	Plazo
1.1 Ventana positiva	🔥🔥🔥	✅✅✅	🔥 Crítica	Inmediato
1.2 Co-ocurrir con ChatGPT	🔥🔥🔥	✅✅✅	🔥 Crítica	Inmediato
1.3 Evitar ruido cripto	🔥🔥	✅✅✅	⚡ Alta	1 mes
1.4 Estacionalidad	🔥🔥	✅✅	⚡ Alta	Continuo
2.1 Integrar ChatGPT API	🔥🔥🔥	✅✅	🔥 Crítica	3-6 meses
2.2 Herramientas prácticas	🔥🔥🔥	✅✅	🔥 Crítica	6-12 meses
2.3 Complementar Bard	🔥🔥	✅✅	⚡ Alta	3-6 meses
2.4 Explicabilidad	🔥🔥	✅	🟡 Media	6-12 meses
3.1 Industrializar pipeline	🔥🔥	✅✅	⚡ Alta	3 meses
3.2 Diccionario NER	🔥🔥	✅✅✅	⚡ Alta	1 mes
3.3 Dashboard continuo	🔥🔥🔥	✅	🟡 Media	3-6 meses
3.4 Interacciones reales	🔥🔥	✅	🟡 Media	6 meses
4.1 Elegir comunidades	🔥🔥🔥	✅✅	🔥 Crítica	Inmediato
4.2 Mercado hispano	🔥🔥🔥	✅✅	⚡ Alta	6-12 meses
4.3 Narrativa balanceada	🔥🔥	✅✅✅	⚡ Alta	Inmediato
5.1 Monitorizar comunidades	🔥🔥	✅✅	🟡 Media	3 meses
5.2 Multimodal	🔥🔥🔥	✅	🟡 Media	12-24 meses
5.3 Regulación	🔥🔥🔥	✅✅	⚡ Alta	2026-2027



Métricas de éxito propuestas (KPI Dashboard)
Objetivo estratégico	KPI	Baseline	Target (12 meses)
Posicionamiento de marca	Share of voice en tweets IA	0%	5%
Sentimiento de marca	Compound VADER	—	≥ +0.25
Alcance orgánico	Engagement rate medio	—	≥ 10 likes/tweet
Comunidades dominadas	Top-3 en comunidad elegida	No	Sí
Adopción producto	Usuarios activos mensuales	0	50,000
Excelencia operativa	Tiempo de re-análisis	20 min	< 10 min
Compliance	% sistemas documentados	0%	100%
Mercado hispano	Presencia top-of-mind	No	Top-5


Consideraciones finales
Estas 17 recomendaciones no son independientes: forman un sistema coherente donde:

Las acciones de marketing (1.x) construyen visibilidad.

Las decisiones de producto (2.x) aprovechan esa visibilidad con propuestas de valor.

La infraestructura de datos (3.x) permite iterar rápido y medir impacto.

La estrategia (4.x) alinea todo con los recursos disponibles.

La innovación (5.x) prepara el futuro.

Prioriza las marcadas como 🔥 Críticas: son las que tienen mayor ROI en el menor plazo.

Revisa este documento cada trimestre para ajustar prioridades según la evolución del mercado.




