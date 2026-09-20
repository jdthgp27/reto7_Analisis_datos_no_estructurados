# Informe de Análisis — Reto 7
## Análisis de 100,000 tweets sobre inteligencia artificial

---

**Curso:** Business Intelligence y Big Data — Curso 6  
**Reto:** 7 — Análisis de Datos No Estructurados y Redes Sociales  
**Analista:** Judit Giravent 
**Fecha de entrega:** Septiembre 2026 
**Repositorio:** `reto7_Analisis_datos_no_estructurados/`

---

## 1. Resumen ejecutivo

Este proyecto analiza **100,000 tweets en inglés** publicados entre el **16 y el 29 de marzo de 2023**, periodo que coincide con la fase de mayor viralidad pública de ChatGPT tras el lanzamiento de GPT-4 (14 de marzo de 2023). Aunque el corpus original abarcaba desde enero, se trabajó con una **muestra de los 100,000 tweets más recientes** por razones de viabilidad computacional, lo que concentra el análisis en la fase más intensa de discusión pública sobre la IA generativa.

Se aplicó un pipeline completo de NLP —limpieza, tokenización, lematización, análisis de sentimiento (VADER + TextBlob), extracción de entidades nombradas (SpaCy), modelado de tópicos (LDA) y análisis de redes de co-ocurrencia— sobre el corpus procesado.

**Los tres hallazgos principales son:**

1. **El sentimiento global hacia la IA es claramente positivo.** El 53.26% de los tweets son positivos frente a un 16.06% de negativos, con un compound medio de VADER de **+0.2174**. El análisis de engagement confirma esta tendencia: los tweets positivos generan **9.49 likes y 1.96 retweets** de media, muy por encima de los negativos (7.23 likes, 1.19 RT) y neutrales (5.82 likes, 0.90 RT).

2. **ChatGPT/OpenAI monopoliza el discurso.** El nodo `gpt` concentra 33,279 menciones y un grado ponderado de 2,344 (más de 4 veces el siguiente), actuando como hub absoluto de la red de co-ocurrencia. Google (1,389), Microsoft (1,079) y Sam Altman (381) completan el pódium de entidades dominantes.

3. **La red de entidades se organiza en 4 comunidades temáticas** claramente diferenciadas: el núcleo OpenAI/ChatGPT, el eje Google-Microsoft-Bard, la esfera política/personalidades, y un grupo periférico de instituciones mediáticas y académicas.

Estos resultados tienen implicaciones directas para estrategias de marketing, desarrollo de producto e inteligencia competitiva en el sector IA, que se detallan en el documento complementario `recomendaciones.md`.

---

## 2. Introducción y objetivos

### 2.1 Contexto

El lanzamiento de ChatGPT (noviembre 2022) y de GPT-4 (marzo 2023) marcó un punto de inflexión en la percepción pública de la inteligencia artificial. Las redes sociales —especialmente Twitter/X— se convirtieron en el principal foro de discusión, con una mezcla de entusiasmo tecnológico, preocupaciones éticas y expectativas económicas.

Entender cómo se articula este discurso permite responder preguntas estratégicas: **¿qué organizaciones dominan la conversación? ¿qué sentimientos genera la IA? ¿qué temas emergen? ¿quiénes son los líderes de opinión?**

### 2.2 Objetivos del análisis

1. **Extraer** un corpus de tweets sobre IA y prepararlo para análisis NLP.
2. **Cuantificar** el sentimiento público (positivo / neutral / negativo) y su evolución.
3. **Identificar** las entidades (organizaciones, personas, productos) mencionadas.
4. **Descubrir** los temas latentes mediante LDA.
5. **Analizar** la estructura de la red de co-ocurrencia de entidades.
6. **Traducir** estos hallazgos en recomendaciones estratégicas.

---

## 3. Metodología resumida

| Fase | Técnica | Herramienta | Output |
|------|---------|-------------|--------|
| **1. Extracción** | Carga y validación de CSV | Pandas | `tweets_ia_raw.csv` |
| **2. Preparación** | Limpieza + tokenización + lematización | SpaCy, NLTK | `tweets_nlp.csv` |
| **3. EDA** | Análisis exploratorio | Matplotlib, Seaborn | 9 figuras |
| **4. Sentimiento** | VADER + TextBlob | NLTK, TextBlob | `tweets_con_sentimiento.csv` |
| **5. NER + Tópicos** | spaCy + LDA | spaCy, scikit-learn | `tweets_entidades.csv`, `lda_temas.csv` |
| **6. Redes** | Co-ocurrencia + Louvain | NetworkX, python-louvain | `red_entidades_*.csv` |

**Detalle completo en** `docs/metodologia.md`.

---

## 4. Análisis exploratorio (EDA)

### 4.1 Volumen y usuarios

- **100,000 tweets** procesados
- **63,418 usuarios únicos** → ratio de 1.58 tweets por usuario, lo que indica un discurso muy atomizado (no hay unos pocos usuarios dominando la conversación)
- **800,135 likes totales** y **151,006 retweets**, con medias de 8.00 likes y 1.51 RT por tweet

Este perfil sugiere un **discurso distribuido**, más de masa que de élite, donde muchos usuarios contribuyen con pocos tweets cada uno.

### 4.2 Evolución temporal

El corpus cubre el periodo **16-29 marzo 2023** (14 días). Este rango coincide con:

- **Lanzamiento de GPT-4** (14 marzo 2023): la conversación está en su punto álgido.
- **Anuncio de Bing Chat con GPT-4** (Microsoft, mediados de marzo).
- **Debate público sobre "pausa de 6 meses"** promovido por Elon Musk y otros.

El análisis temporal (ver `03_tweets_por_dia.png`) muestra una **actividad sostenida** en todo el periodo, sin picos excepcionales, lo que indica que el tema ya estaba consolidado en la agenda pública en esas fechas.

### 4.3 Engagement

La distribución de likes y retweets (ver `03_engagement_distribucion.png`) es **fuertemente asimétrica**: la mayoría de tweets tienen 0-5 likes, mientras que una minoría concentra cientos o miles. Esto es típico de Twitter/X y sugiere que **los tweets virales son excepcionales**, no la norma.

### 4.4 Vocabulario dominante

Los términos más frecuentes (ver `03_top_30_palabras.png`) están dominados por:

- **"chatgpt"** y **"gpt"** — omnipresentes
- **"google"**, **"microsoft"**, **"bard"** — competidores directos
- **"ai"**, **"artificial"**, **"intelligence"** — términos genéricos
- **"nft"**, **"crypto"** — comunidad tangencial

---

## 5. Análisis de sentimiento

### 5.1 Distribución global

| Sentimiento | Tweets | Porcentaje |
|-------------|--------|-----------|
| 🟢 Positivo | 53,260 | **53.26%** |
| ⚪ Neutral | 30,678 | **30.68%** |
| 🔴 Negativo | 16,062 | **16.06%** |

**Compound medio (VADER):** +0.2174  
**Desviación estándar:** 0.4081

El resultado es **inequívoco**: el discurso dominante sobre IA en este periodo es **optimista**. Menos de uno de cada cinco tweets es negativo, y el compound medio es claramente positivo.

### 5.2 Engagement por sentimiento

| Sentimiento | Likes (media) | Retweets (media) |
|-------------|---------------|------------------|
| 🟢 Positivo | **9.49** | **1.96** |
| 🔴 Negativo | 7.23 | 1.19 |
| ⚪ Neutral | 5.82 | 0.90 |

**Hallazgo relevante:** Los tweets **positivos** generan **un 24% más de likes** que los negativos y un **64% más de retweets**. Esto contradice la intuición común de que "las malas noticias se comparten más". En el discurso IA de marzo 2023, **el entusiasmo moviliza más que la crítica**.

### 5.3 Interpretación

Tres hipótesis explican este patrón:

1. **Fase de novedad positiva:** GPT-4 acababa de lanzarse y las demostraciones impresionaban.
2. **Sesgo de adopción temprana:** los usuarios activos de Twitter en marzo 2023 eran mayoritariamente *early adopters* tecnológicos.
3. **Contenido viral positivo:** los hilos demostrativos ("mira lo que hizo ChatGPT") generaban más engagement que las críticas, que suelen ser más matizadas.

---

## 6. Extracción de entidades (NER)

### 6.1 Organizaciones dominantes

| Entidad | Menciones |
|---------|-----------|
| **gpt** | 33,279 |
| google | 1,389 |
| microsoft | 1,079 |
| gpt gpt | 302 |
| gm | 229 |

> ⚠️ **Nota metodológica:** spaCy clasificó `gpt` como ORG (por contexto) y separó mal algunos términos (`gpt gpt`, `google s`). Se documenta como limitación.

### 6.2 Personas mencionadas

| Persona | Menciones |
|---------|-----------|
| **sam altman** | 381 |
| midjourney openai | 162 |

> ⚠️ `don`, `doesn` son falsos positivos por contracciones inglesas. `Sam Altman` (CEO de OpenAI) es el único líder claramente identificado.

### 6.3 Productos

| Producto | Menciones |
|----------|-----------|
| google s | 160 |
| google s bard | 93 |
| google microsoft | 46 |

### 6.4 Interpretación

El **99% del "volumen de entidades" gira alrededor de ChatGPT/OpenAI**. Sam Altman es la única persona que emerge con fuerza individual, confirmando su rol como **portavoz público de la IA generativa** durante marzo 2023.

Google y Microsoft aparecen como **retadores**, con Bard (Google) y Bing Chat (Microsoft) mencionados en el contexto de "competencia con ChatGPT".

---

## 7. Modelado de tópicos (LDA)

Con 8 temas detectados sobre 94,653 tweets, se identificaron los siguientes patrones temáticos:

| Tema | Palabras clave | Interpretación | Tweets |
|------|----------------|----------------|--------|
| **0** | language, artificialintelligence, write, model, prompt, midjourney | **IA generativa y escritura** | 12,573 |
| **1** | chatbot, airdrop, tool, right, technology, business | **Herramientas y chatbots** | 11,142 |
| **2** | airdrop nft, copilot, eth, programming, usdc | **Cripto + IA (nicho)** | 5,352 |
| **3** | chat, time, future, powerful, human | **Futuro y capacidades** | 11,624 |
| **4** | chat, ask, intelligence, artificial, world | **Uso general y preguntas** | 16,980 |
| **5** | chat, microsoft, bing, crypto, writing, video | **Microsoft/Bing + marketing** | 19,085 |
| **6** | nft, learn, machinelearning, game, api | **Aprendizaje y juegos** | 5,971 |
| **7** | google, bard, work, tech, education, thanks | **Google Bard y educación** | 11,926 |

### 7.1 Observaciones

1. **El tema más voluminoso (Tema 5, 19,085 tweets) mezcla IA + cripto + marketing**, lo que revela la presencia significativa de comunidades cripto que adoptan IA como herramienta de generación de contenido.

2. **Los temas de IA "pura"** (0, 3, 4, 7) suman ~53,000 tweets, la mitad del corpus.

3. **La comunidad cripto-IA** (temas 2 y 6) suman ~11,300 tweets, un nicho relevante pero minoritario.

4. **Google Bard** aparece como tema propio (Tema 7), confirmando que la competencia OpenAI vs. Google es un eje discursivo de primer orden.

---

## 8. Análisis de redes sociales

### 8.1 Red de co-ocurrencia de entidades

Se construyó una red de entidades (ORG, PERSON, PRODUCT) con **frecuencia ≥ 20 apariciones**, donde cada arista representa una co-ocurrencia en el mismo tweet.

**Características de la red:**

- **Nodos:** 77
- **Aristas:** 254
- **Comunidades detectadas (Louvain):** 4

### 8.2 Hubs principales

| Entidad | Tipo | Frecuencia | Grado ponderado | Betweenness |
|---------|------|------------|-----------------|-------------|
| **gpt** | ORG | 33,279 | **2,344** | 0.324 |
| google | ORG | 1,389 | 521 | 0.134 |
| microsoft | ORG | 1,079 | 447 | 0.080 |
| don | PERSON | 982 | 342 | 0.273 |
| doesn | PERSON | 554 | 242 | 0.176 |
| sam altman | PERSON | 381 | 206 | 0.085 |
| gpt gpt | ORG | 302 | 157 | 0.058 |
| gm | ORG | 229 | 133 | 0.009 |

> **gpt** es un **hub absoluto**: su grado ponderado es **4.5 veces superior** al siguiente nodo (google). Esto confirma la **centralización extrema** del discurso en torno a ChatGPT.

> **Betweenness alto en `don` y `doesn`** (0.27 y 0.18) refleja que, siendo artefactos de la contracción inglesa "don't/doesn't", aparecen en muchísimos tweets sobre IA (porque se habla de lo que la IA "no puede hacer"). Es un artefacto técnico.

### 8.3 Comunidades detectadas

**Comunidad 0 (45 nodos) — "Núcleo OpenAI/ChatGPT"**
- Entidades: `gpt`, `sam altman`, `chatgpt plus premium account`, `gm`, `joe`
- Representa el ecosistema OpenAI: producto, CEO, usuarios premium y menciones coloquiales.

**Comunidad 1 (19 nodos) — "Eje Google-Microsoft-Bard"**
- Entidades: `google`, `microsoft`, `bard`, `seo`, `google s`
- Representa la **competencia directa**: Google Bard, Microsoft Bing Chat y el ecosistema SEO/marketing.

**Comunidad 2 (6 nodos) — "Política y personalidades"**
- Entidades: `un`, `donald trump`, `khan`, `marketsoup chatgpt`
- Representa el **discurso geopolítico** alrededor de la IA.

**Comunidad 3 (7 nodos) — "Instituciones y medios"**
- Entidades: `stanford`, `cnn`, `apple`, `genie`, `chat gpt`
- Representa el discurso **académico y mediático**.

### 8.4 Interpretación

La red revela una **estructura "hub-and-spoke"**: un nodo central (ChatGPT) conecta todas las comunidades, que orbitan a su alrededor con temáticas específicas.

Esto tiene implicaciones estratégicas:

- **Cualquier actor que quiera posicionarse en el discurso IA debe co-ocurrir con ChatGPT** en los tweets, o quedará invisible en la red.
- **Google y Microsoft** forman una comunidad propia porque su discurso se articula como "alternativas a ChatGPT", no como discurso independiente.
- **La política, los medios y la academia** son comunidades periféricas: la IA todavía no se ha "politizado" del todo en marzo 2023.

---

## 9. Conclusiones

1. **El sentimiento público hacia la IA en marzo 2023 era marcadamente positivo** (53.26% positivo, compound +0.217), con el engagement reforzando esta tendencia: los tweets positivos obtienen un 64% más de retweets que los negativos.

2. **ChatGPT/OpenAI domina el discurso de forma casi monopólica.** El nodo `gpt` tiene un grado ponderado de 2,344, 4.5 veces superior al siguiente (Google, 521). OpenAI no compite: lidera.

3. **La competencia OpenAI vs. Google es el segundo eje discursivo.** Bard, Microsoft y Bing Chat forman una comunidad temática propia de 19 nodos, articulada como "alternativa al líder".

4. **La comunidad cripto-IA es un nicho significativo pero minoritario** (~11,300 tweets en los temas 2 y 6 del LDA). Revela una **convergencia emergente** entre IA generativa y generación de contenido NFT.

5. **Sam Altman es la única persona con presencia destacada** como entidad individual, confirmando su rol como portavoz público de la IA generativa.

6. **La red de entidades se estructura en 4 comunidades** (OpenAI, Google-Microsoft, política, medios/academia), con ChatGPT como hub central conectando todas ellas.

7. **El análisis bilingüe es marginal:** el 99.77% de los tweets son en inglés. El español apenas representa el 0.23% del corpus, lo que limita cualquier conclusión sobre el discurso hispanohablante.

---

## 10. Limitaciones

Este análisis tiene limitaciones que condicionan la interpretación de los resultados. Se documentan con transparencia:

### 10.1 Sesgo temporal severo
El corpus efectivo cubre **solo 14 días (16-29 marzo 2023)**, no los 3 meses originales. Esto se debe a que se procesó `df.head(100,000)` sobre el CSV ordenado descendentemente. **No se puede hablar de "evolución del sentimiento" ni de "tendencias"** con rigor. Los hallazgos describen un **fotograma**, no una película.

### 10.2 Ruido en NER
spaCy `en_core_web_sm` generó falsos positivos:
- `don`, `doesn` (contracciones inglesas)
- `gpt gpt`, `gpt gpt gpt` (fragmentos mal extraídos)
- `google s`, `microsoft s` (posesivos ingleses)

Impacto: **moderado en el análisis de entidades**, bajo en las conclusiones generales (ChatGPT sigue dominando incluso tras filtrar el ruido).

### 10.3 Desequilibrio lingüístico extremo
Solo 229 tweets en español (0.23%). El pipeline bilingüe (SpaCy es + en) no aporta valor real en este corpus.

### 10.4 Red pequeña
77 nodos y 254 aristas es una red de tamaño modesto. Con umbral `MIN_FREQ=10` se habrían obtenido más nodos, pero también más ruido.

### 10.5 Análisis de redes por co-ocurrencia, no por interacción
La red refleja proximidad temática, no interacciones reales (retweets, replies, menciones). **No se puede inferir influencia social** sino proximidad discursiva.

### 10.6 Sentimiento sin ground truth
VADER y TextBlob son modelos genéricos, no entrenados específicamente en el dominio IA. No se validaron contra un ground truth del corpus.

### 10.7 Sin análisis multimedia
No se procesaron imágenes, vídeos ni enlaces externos asociados a los tweets. Los memes y demostraciones visuales (muy relevantes en IA) quedan fuera.

---

## 11. Próximos pasos sugeridos

Para una segunda iteración, se recomienda:

1. **Reprocesar el corpus completo (500k tweets)** con muestreo aleatorio estratificado por fecha para evitar el sesgo temporal.
2. **Ampliar el corpus con datos actualizados (2024-2026)** para capturar la evolución del discurso.
3. **Mejorar el NER** con un diccionario específico del dominio IA (entidades conocidas + aliases).
4. **Aplicar BERT o RoBERTa** para sentimiento específico del dominio tecnológico.
5. **Incorporar análisis de imágenes** (memes, capturas, gráficos) mediante OCR + clasificación visual.
6. **Combinar co-ocurrencia con interacciones reales** (retweets, replies) usando Twitter API (si se dispone de plan de pago).

---

## 12. Anexos

- **Figuras:** `outputs/figuras/` (25+ imágenes)
- **Datos procesados:** `data/processed/` (10+ CSV + GEXF para Gephi)
- **Reportes intermedios:** `outputs/reportes/`
- **Metodología completa:** `docs/metodologia.md`
- **Recomendaciones estratégicas:** `docs/recomendaciones.md`
- **Selección de fuentes:** `docs/seleccion_fuentes.md`

---

*Informe generado como parte del Reto 7 del Curso 6 de Business Intelligence y Big Data.*