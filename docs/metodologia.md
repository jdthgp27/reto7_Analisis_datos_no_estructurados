
---



```markdown
# Metodología Detallada — Reto 7
## Pipeline completo de análisis de datos no estructurados

---

**Curso:** Business Intelligence y Big Data — Curso 6  
**Reto:** 7 — Análisis de Datos No Estructurados y Redes Sociales  
**Analista:** Judit Giravent
**Fecha:** Septiembre 2026
**Repositorio:** `reto7_Analisis_datos_no_estructurados/`

---

## 1. Visión general del proyecto

Este documento describe **en detalle** el pipeline técnico implementado para el análisis de 100,000 tweets sobre IA. Cubre desde la extracción de datos hasta la generación de insights, incluyendo las **decisiones técnicas** y sus justificaciones.

El proyecto se estructura en **7 notebooks** que corresponden a las 7 fases del reto, con artefactos intermedios guardados en `data/processed/` para garantizar trazabilidad y reproducibilidad.

---

## 2. Arquitectura del pipeline

┌─────────────────────────────────────────────────────────────────┐
│ FUENTES DE DATOS (RAW) │
│ Twitter Jan Mar.csv (500k) | ai_tweet.csv | sentiment/ │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 01 — EXTRACCIÓN Y VALIDACIÓN │
│ • Carga CSV con encoding auto-detectado │
│ • Validación de esquema │
│ • Análisis de nulos │
│ Output: tweets_ia_raw_YYYYMMDD.csv │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 02 — PREPARACIÓN DE DATOS │
│ • Limpieza (URLs, menciones, hashtags, emojis) │
│ • Normalización (lowercase, strip) │
│ • Tokenización + stopwords (en+es+custom) │
│ • Lematización SpaCy bilingüe │
│ Output: tweets_limpios_YYYYMMDD.csv, tweets_nlp_YYYYMMDD.csv │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 03 — ANÁLISIS EXPLORATORIO (EDA) │
│ • Distribución temporal │
│ • Frecuencia de términos │
│ • WordClouds │
│ • Distribución de engagement │
│ Output: 9 figuras PNG en outputs/figuras/03_* │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 04 — NLP Y SENTIMIENTO │
│ • VADER (compound, pos/neu/neg) │
│ • TextBlob (polarity, subjectivity) │
│ • Clasificación + análisis por segmentos │
│ Output: tweets_con_sentimiento_YYYYMMDD.csv │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 05 — NER Y LDA │
│ • NER con SpaCy (en_core_web_sm) │
│ • LDA con scikit-learn (8 temas) │
│ Output: tweets_entidades_.csv, lda_temas_.csv │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 06 — ANÁLISIS DE REDES │
│ • Red de co-ocurrencia de entidades │
│ • Centralidades (grado, betweenness, closeness) │
│ • Detección de comunidades (Louvain) │
│ Output: red_entidades_.csv, red_entidades_.gexf │
└───────────────────────────┬─────────────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────────┐
│ 07 — INTERPRETACIÓN Y RECOMENDACIONES │
│ • Dashboard resumen │
│ • Informe consolidado │
│ • Recomendaciones estratégicas │
│ Output: informe_analisis.md, recomendaciones.md │
└─────────────────────────────────────────────────────────────────┘



---

## 3. Detalle por fase

### 3.1 Fase 1 — Extracción y validación (Notebook 01)

**Objetivos:**
- Cargar el corpus principal y validar su integridad
- Identificar el esquema de columnas
- Documentar el rango temporal y volumen

**Decisiones técnicas:**

| Decisión | Opción elegida | Alternativa | Justificación |
|----------|---------------|-------------|---------------|
| Carga de CSV | `pd.read_csv` con `encoding='utf-8'` + fallback a `latin-1` | `dask.read_csv` | El tamaño (111 MB) cabe en RAM |
| Validación | `df.info()`, `df.dtypes`, `df.isnull().sum()` | `pandera`, `great_expectations` | Suficiente para el volumen |
| Muestreo | `df.head(100_000)` | `df.sample(100_000, random_state=42)` | **⚠️ Esto causó sesgo temporal — ver limitaciones** |

**Resultados:**
- Corpus: 500,036 tweets (ene-mar 2023)
- Muestra procesada: 100,000 tweets
- Ratio de compresión: 20%

---

### 3.2 Fase 2 — Preparación de datos (Notebook 02)

**Pipeline de limpieza aplicado:**

```python
def limpiar_texto(texto):
    texto = texto.lower()                          # 1. Normalización
    texto = quitar_urls(texto)                     # 2. URLs
    texto = quitar_menciones(texto)                # 3. @usuario
    texto = quitar_hashtags(texto)                 # 4. #hashtag (mantiene el texto)
    texto = quitar_emojis(texto)                   # 5. Emojis
    texto = quitar_numeros(texto)                  # 6. Números
    texto = re.sub(r"[^a-záéíóúñü\s]", " ", texto) # 7. Símbolos
    texto = re.sub(r"\s+", " ", texto).strip()     # 8. Espacios
    return texto

```
Stopwords utilizadas:

Español: 313 (NLTK)

Inglés: 198 (NLTK)

Custom: 52 (URLs, ruido técnico)

Total: 553

⚠️ Decisión revertida: Originalmente se incluyeron chatgpt, openai, gpt en stopwords custom, pero se revirtió porque son términos clave del dominio.

Lematización:

Modelo	Uso	Observación
en_core_web_sm	Tweets en inglés	✅ Correcto
es_core_news_sm	Tweets en español	⚠️ Generó ruido (writtir, peoplir)
Detección de idioma:
Heurística simple basada en:

Presencia de caracteres españoles (áéíóúñ¿¡)

Ratio de palabras funcionales españolas

Resultado: 99.77% clasificados como inglés, 0.23% como español.

3.3 Fase 3 — Análisis exploratorio (Notebook 03)
Análisis realizados:

Análisis	Método	Output
Volumen temporal	groupby(date).size()	03_tweets_por_dia.png
Top palabras	Counter sobre tokens	03_top_30_palabras.png
Top bigramas	CountVectorizer(ngram_range=(1,2))	03_top_bigramas.png
Top trigramas	CountVectorizer(ngram_range=(1,3))	03_top_trigramas.png
WordCloud por tema	WordCloud	03_wordcloud_chatgpt.png
Distribución engagement	Histograma	03_engagement_distribucion.png
Insight principal: El corpus es altamente asimétrico en engagement — la mayoría de tweets tienen 0-5 likes, con una minoría viral.

3.4 Fase 4 — NLP y sentimiento (Notebook 04)
Modelos utilizados:

VADER (Valence Aware Dictionary and sEntiment Reasoner):

Modelo basado en léxico

Diseñado específicamente para redes sociales (emojis, jerga, intensificadores)

Output: compound (-1 a +1) + pos, neu, neg

TextBlob:

Basado en Naive Bayes + Pattern

Output: polarity (-1 a +1) + subjectivity (0 a 1)

Más lento que VADER

Clasificación:

def clasificar(compound, umbral=0.05):
    if compound >= umbral:
        return "positivo"
    elif compound <= -umbral:
        return "negativo"
    return "neutral"

¿Por qué VADER y no BERT?

VADER: rápido, ligero, entrenado en redes sociales

BERT: más preciso pero requiere GPU, entrenamiento específico, ~10x más lento

Para 100k tweets en un portátil, VADER es la elección pragmática

Resultados:

53.26% positivo / 30.68% neutral / 16.06% negativo

Compound medio: +0.2174

3.5 Fase 5 — NER y LDA (Notebook 05)
NER con SpaCy:

Modelo: en_core_web_sm (no trf ni lg por tamaño)

Tipos extraídos: PERSON, ORG, GPE, PRODUCT, EVENT, WORK_OF_ART, NORP, MONEY

Tiempo de procesamiento: ~8 minutos para 100k tweets

Análisis crítico del NER:

Entidad detectada	Tipo	Problema
don	PERSON	Falso positivo (contracción "don't")
doesn	PERSON	Falso positivo (contracción "doesn't")
gpt gpt	ORG	Fragmentación incorrecta
google s	PRODUCT	Posesivo inglés mal separado
sam altman	PERSON	✅ Correcto
Precisión estimada: ~70% (aceptable para análisis exploratorio, mejorable con diccionario).

LDA con scikit-learn:

Parámetros elegidos:

LatentDirichletAllocation(
    n_components=8,          # 8 temas (balance entre granularidad y coherencia)
    max_iter=15,             # Suficiente para convergencia en este corpus
    learning_method="online",# Más rápido para datasets grandes
    random_state=42,         # Reproducibilidad
    n_jobs=-1,               # Usar todos los cores
)

Vectorización:

CountVectorizer(
    max_df=0.95,             # Ignorar términos en >95% de docs (stopwords residuales)
    min_df=5,                # Ignorar términos en <5 docs (ruido)
    max_features=3000,       # Top 3000 términos
    ngram_range=(1, 2),      # Unigramas y bigramas
    stop_words="english",    # Refuerzo de stopwords
)

Perplexity obtenido: 1726.15 (razonable para LDA con 8 temas en 94k docs)

Temas detectados: 8, con volúmenes entre 5,352 y 19,085 tweets.

3.6 Fase 6 — Análisis de redes (Notebook 06)
Enfoque elegido: Red de co-ocurrencia de entidades (Enfoque A).

Construcción del grafo:

# Filtrado de entidades
TIPOS_INCLUIDOS = {"ORG", "PERSON", "PRODUCT"}
MIN_FREQ = 20

# Co-ocurrencia: para cada tweet, combinar entidades válidas en pares
for ents in df["entidades_parsed"]:
    entidades_tweet = list({e for e, _ in ents if e in entidades_validas})
    for par in combinations(sorted(entidades_tweet), 2):
        conteo_pares[par] += 1

Parámetros y justificación:

Parámetro	Valor	Justificación
Tipos incluidos	ORG, PERSON, PRODUCT	Excluir GPE para red temática limpia
MIN_FREQ	20	Balance entre cobertura y ruido
Nodos resultantes	77	Manejable para análisis y visualización
Aristas resultantes	254	Suficientes para estructura significativa
Métricas de centralidad:

Métrica	Qué mide	Uso
Grado ponderado	Volumen de conexiones	Identifica hubs
Betweenness	Frecuencia de paso en caminos cortos	Identifica puentes
Closeness	Cercanía media al resto	Identifica nodos centrales
Eigenvector	Importancia por conexión a otros importantes	Identifica poder estructural
Detección de comunidades:

Algoritmo: Louvain (Blondel et al., 2008)

Implementación: python-louvain

Ventajas: rápido, escalable, no requiere número de comunidades predefinido

Resultado: 4 comunidades detectadas

Exportación a Gephi: archivo .gexf para visualización interactiva.

3.7 Fase 7 — Interpretación (Notebook 07)
Consolidación de métricas:

Todos los números clave en un diccionario metricas

Dashboard visual con 6 paneles clave

Generación de informes:

docs/informe_analisis.md: 12 secciones detalladas

docs/recomendaciones.md: 17 recomendaciones priorizadas

docs/metodologia.md: este documento

outputs/reportes/07_resumen_ejecutivo.md: síntesis

4. Decisiones técnicas clave
4.1 ¿Por qué muestrear 100k en lugar de procesar 500k?
Ventajas:

5x menos tiempo de procesamiento (~20 min vs. 100 min)

Menos memoria RAM (2-3 GB vs. 12-15 GB)

Suficiente para análisis estadísticamente robusto

Desventajas:

Sesgo temporal (el corpus se ordena por fecha y se toma head())

Pérdida de tweets minoritarios

Lección aprendida: Para futuras iteraciones, usar df.sample(100_000, random_state=42) para evitar el sesgo.

4.2 ¿Por qué SpaCy y no otros NLP?
Aspecto	SpaCy	NLTK	Stanford NLP	Hugging Face
Velocidad	⚡⚡⚡	🐢	🐢	⚡⚡
Precisión NER	⚡⚡	⚡	⚡⚡⚡	⚡⚡⚡
Facilidad de uso	⚡⚡⚡	⚡⚡	🐢	⚡⚡
Modelos listos	⚡⚡⚡	⚡	⚡⚡	⚡⚡⚡
SpaCy es el mejor balance velocidad / precisión / facilidad para este volumen.

4.3 ¿Por qué VADER y no BERT para sentimiento?
Aspecto	VADER	BERT	RoBERTa
Velocidad	⚡⚡⚡ (100k tweets en 2 min)	🐢 (GPU necesaria, ~30 min)	🐢
Precisión genérica	⚡⚡⚡	⚡⚡⚡	⚡⚡⚡
Precisión en tweets	⚡⚡⚡ (diseñado para ello)	⚡⚡	⚡⚡
Requisitos	CPU, RAM normal	GPU, 8+ GB VRAM	Similar
Interpretabilidad	Alta (léxico)	Baja (caja negra)	Baja
VADER es el estándar de facto en análisis de tweets académicos por su combinación de velocidad, precisión y ligereza.

4.4 ¿Por qué Louvain y no Leiden o Girvan-Newman?
Algoritmo	Velocidad	Calidad	Requisitos
Louvain	⚡⚡⚡	⚡⚡⚡	Ninguno
Leiden	⚡⚡⚡	⚡⚡⚡⚡ (mejora Louvain)	python-igraph
Girvan-Newman	🐢 (O(n³))	⚡⚡⚡	Grafo pequeño
Label Propagation	⚡⚡⚡⚡	⚡⚡	Menos estable
Louvain es el estándar para redes de cientos a miles de nodos. Leiden es una mejora pero requiere python-igraph y no aporta mucho más en nuestro tamaño.

5. Herramientas y dependencias
5.1 Entorno
Python: 3.13.7

Sistema: Windows 11

Kernel Jupyter: reto7_ia

5.2 Librerías principales

# Datos
pandas==2.2.0
numpy==1.26.0

# NLP
nltk==3.8.1
spacy==3.7.2
textblob==0.18.0
en-core-web-sm==3.7.1
es-core-news-sm==3.7.0

# Machine Learning
scikit-learn==1.4.0

# Redes
networkx==3.2.1
python-louvain==0.16

# Visualización
matplotlib==3.8.2
seaborn==0.13.0
wordcloud==1.9.2

# Utilidades
tqdm==4.66.1

5.3 Instalación

pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm

6. Estructura del repositorio

reto7_Analisis_datos_no_estructurados/
│
├── data/
│   ├── raw/
│   │   └── tweets/
│   │       ├── ai_tweet.csv               (1.4 MB)
│   │       ├── Twitter Jan Mar.csv        (111.6 MB)
│   │       └── sentiment/file.csv         (33.6 MB)
│   │
│   └── processed/
│       ├── tweets_ia_raw_20260920.csv     (116 MB)
│       ├── tweets_limpios_20260920.csv    (60 MB)
│       ├── tweets_nlp_20260920.csv        (41 MB)
│       ├── tweets_con_sentimiento_*.csv   (~45 MB)
│       ├── tweets_entidades_*.csv         (~15 MB)
│       ├── tweets_topicos_*.csv           (~5 MB)
│       ├── lda_temas_*.csv
│       ├── red_entidades_nodos_*.csv
│       ├── red_entidades_aristas_*.csv
│       ├── red_entidades_comunidades_*.csv
│       └── red_entidades_*.gexf
│
├── notebooks/
│   ├── 01_extraccion_tweets.ipynb
│   ├── 02_preparacion_datos.ipynb
│   ├── 03_eda_visualizacion.ipynb
│   ├── 04_nlp_sentimientos.ipynb
│   ├── 05_ner_lda.ipynb
│   ├── 06_analisis_redes.ipynb
│   └── 07_interpretacion_recomendaciones.ipynb
│
├── src/
│   ├── __init__.py
│   ├── extraccion/
│   ├── preparacion/
│   ├── analisis/
│   └── utilidades/
│
├── outputs/
│   ├── figuras/                            (25+ PNG)
│   ├── modelos/
│   └── reportes/                           (7 MD)
│
├── docs/
│   ├── informe_analisis.md
│   ├── recomendaciones.md
│   ├── metodologia.md
│   └── seleccion_fuentes.md
│
├── requirements.txt
└── README.md

7. Reproducibilidad
7.1 Ejecución completa
Para reproducir el análisis desde cero:

# 1. Clonar repositorio
git clone [URL_DEL_REPO]
cd reto7_Analisis_datos_no_estructurados

# 2. Crear entorno virtual
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # Linux/Mac

# 3. Instalar dependencias
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python -m spacy download es_core_news_sm

# 4. Ejecutar notebooks en orden
jupyter notebook
# Abrir y ejecutar: 01 → 02 → 03 → 04 → 05 → 06 → 07

7.2 Tiempos estimados
Notebook	Tiempo de ejecución
01 — Extracción	< 2 min
02 — Preparación	10-15 min
03 — EDA	3-5 min
04 — NLP	5-8 min
05 — NER + LDA	10-15 min
06 — Redes	5-8 min
07 — Interpretación	2-3 min
Total	~40-55 min
7.3 Requisitos hardware
Mínimo: CPU 4 cores, 8 GB RAM, 10 GB disco

Recomendado: CPU 8+ cores, 16 GB RAM, 20 GB disco SSD

GPU: opcional (no utilizada)

8. Limitaciones metodológicas
Documentadas con transparencia:

8.1 Sesgo temporal en la muestra
Problema: df.head(100_000) sobre CSV ordenado descendentemente → solo 14 días de marzo 2023.

Impacto: Alto — las conclusiones describen un fotograma, no una evolución.

Solución futura: df.sample(n=100_000, random_state=42) o estratificar por fecha.

8.2 Ruido en NER
Problema: spaCy generó falsos positivos (don, doesn, gpt gpt).

Impacto: Moderado — ChatGPT sigue dominando incluso tras filtrar.

Solución futura: Diccionario específico del dominio + reglas de limpieza.

8.3 Desequilibrio lingüístico
Problema: 99.77% inglés, 0.23% español.

Impacto: El pipeline bilingüe no aporta valor en este corpus.

Solución futura: Adquirir corpus hispanohablante específico.

8.4 Red de tamaño modesto
Problema: 77 nodos por MIN_FREQ=20.

Impacto: La red es interpretable pero pierde matices minoritarios.

Solución futura: MIN_FREQ=10 con filtrado manual posterior.

8.5 Sentimiento sin ground truth específico
Problema: VADER y TextBlob no se validaron contra corpus etiquetado del dominio IA.

Impacto: Precisión desconocida (aunque VADER está validado en redes sociales genéricamente).

Solución futura: Validar contra sentiment/file.csv (219k etiquetados) del corpus original.

8.6 Co-ocurrencia vs. interacción real
Problema: La red refleja proximidad temática, no influencia social.

Impacto: No se puede hablar de "influencers" en sentido estricto.

Solución futura: Extraer retweets, replies, menciones desde Twitter API.

9. Buenas prácticas aplicadas
✅ Reproducibilidad: timestamps en archivos, seeds fijos, entorno documentado
✅ Modularidad: separación en notebooks por fase, artefactos intermedios
✅ Documentación: cada decisión técnica justificada
✅ Escalabilidad: código parametrizable, batch processing con SpaCy
✅ Transparencia: limitaciones documentadas explícitamente
✅ Exportación: GEXF para Gephi, CSV para análisis externo

10. Trabajo futuro propuesto
10.1 Corto plazo (1-3 meses)
□ Corregir sesgo temporal con muestreo estratificado
□ Validar sentimiento contra ground truth
□ Industrializar pipeline a scripts src/
10.2 Medio plazo (3-6 meses)
□ Ampliar corpus a 500k tweets completos
□ Incorporar análisis de interacciones reales (retweets, replies)
□ Migrar sentimiento a BERT/RoBERTa para mayor precisión
10.3 Largo plazo (6-12 meses)
□ Análisis multimodal (imágenes, videos)
□ Dashboard de monitorización continua
□ Análisis comparativo multi-año (2023 vs. 2024 vs. 2025)
11. Referencias técnicas
Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. ICWSM.

Blei, D.M., Ng, A.Y., & Jordan, M.I. (2003). Latent Dirichlet Allocation. JMLR.

Blondel, V.D. et al. (2008). Fast unfolding of communities in large networks. J. Stat. Mech.

Honnibal, M. & Montani, I. (2017). spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing.

Loria, S. (2018). TextBlob: Simplified Text Processing.

Hagberg, A. et al. (2008). Exploring network structure, dynamics, and function using NetworkX.

