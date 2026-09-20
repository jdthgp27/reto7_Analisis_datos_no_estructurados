
---

## 📄 `docs/seleccion_fuentes.md` — Versión ampliada

```markdown
# Selección de Fuentes de Datos — Reto 7
## Criterios, justificación y evaluación de las fuentes utilizadas

---

**Curso:** Business Intelligence y Big Data — Curso 6  
**Reto:** 7 — Análisis de Datos No Estructurados y Redes Sociales  
**Analista:** Judit Giravent
**Fecha:** Septiembre 2026

---

## 1. Introducción

Uno de los primeros desafíos del reto fue **identificar y seleccionar las fuentes de datos** adecuadas para el análisis de datos no estructurados. Este documento documenta:

1. **Qué fuentes** se consideraron (y por qué)
2. **Qué fuentes** se seleccionaron finalmente
3. **Qué criterios** guiaron la decisión
4. **Qué limitaciones** tiene cada fuente

---

## 2. Fuentes consideradas

### 2.1 Opción A: Web scraping en vivo (Twitter/X)

**Descripción:** Extraer tweets en tiempo real mediante la API de Twitter/X o scraping.

| Aspecto | Evaluación |
|---------|-----------|
| **Ventaja** | Datos frescos, actualizados |
| **Ventaja** | Posibilidad de capturar interacciones (retweets, replies) |
| **Desventaja** | Requiere API paga ($100-5000/mes) |
| **Desventaja** | Time-consuming (setup + scraping) |
| **Desventaja** | Rate limits severos desde 2023 |
| **Desventaja** | Riesgo de bloqueo de cuenta |
| **Decisión** | ❌ No elegida (coste + complejidad) |

---

### 2.2 Opción B: Datasets públicos de Kaggle

**Descripción:** Descargar corpora ya curados de Kaggle sobre IA/ChatGPT.

| Aspecto | Evaluación |
|---------|-----------|
| **Ventaja** | Gratis, acceso inmediato |
| **Ventaja** | Ya curados y validados por la comunidad |
| **Ventaja** | Múltiples datasets complementarios |
| **Desventaja** | Datos "congelados" (no actualizados) |
| **Desventaja** | Pueden tener sesgos del autor original |
| **Decisión** | ✅ **Elegida** |

---

### 2.3 Opción C: Noticias y artículos de prensa

**Descripción:** Extraer noticias de medios (NYT, Guardian, El País) sobre IA.

| Aspecto | Evaluación |
|---------|-----------|
| **Ventaja** | Contenido de calidad, contextualizado |
| **Ventaja** | Fácil de scrapear (RSS, APIs) |
| **Desventaja** | Volumen limitado |
| **Desventaja** | No refleja opinión pública masiva |
| **Desventaja** | Sesgo editorial de cada medio |
| **Decisión** | ❌ No elegida (no es representativa de opinión pública) |

---

### 2.4 Opción D: Reddit (subreddits de IA)

**Descripción:** Extraer posts y comentarios de r/artificial, r/ChatGPT, r/singularity.

| Aspecto | Evaluación |
|---------|-----------|
| **Ventaja** | Comunidad técnica, alta calidad |
| **Ventaja** | API pública (PRAW) |
| **Ventaja** | Contiene hilos largos y discusiones profundas |
| **Desventaja** | Sesgo hacia usuarios técnicos |
| **Desventaja** | Formato distinto a Twitter (comentarios anidados) |
| **Decisión** | ⚠️ Considerada como complemento |

---

## 3. Fuentes seleccionadas (decisión final)

### 3.1 Corpus principal: `Twitter Jan Mar.csv`

| Atributo | Valor |
|----------|-------|
| **Origen** | Kaggle — autor `khalidryder777` |
| **Volumen** | 500,036 tweets |
| **Periodo** | Enero-Marzo 2023 |
| **Idioma principal** | Inglés |
| **Tamaño del archivo** | 111.6 MB |
| **Licencia** | Pública (CC-BY) |
| **URL** | [kaggle.com/datasets/khalidryder777/500k-chatgpt-tweets-jan-mar-2023] |

**Columnas:**
- `date` — timestamp del tweet
- `id` — ID único
- `content` — texto del tweet
- `username` — autor
- `like_count` — likes
- `retweet_count` — retweets

**Justificación:**
- **Volumen adecuado:** 500k tweets es suficiente para análisis estadístico robusto.
- **Periodo relevante:** Cubre el lanzamiento y masificación de ChatGPT.
- **Formato limpio:** Columnas bien estructuradas, sin ruido innecesario.
- **Metadata completa:** Incluye engagement (likes, retweets) para análisis adicional.
- **Temática alineada:** Todos los tweets mencionan ChatGPT o IA.

---

### 3.2 Corpus complementario: `sentiment/file.csv`

| Atributo | Valor |
|----------|-------|
| **Origen** | Kaggle — autor `charunisa` |
| **Volumen** | 219,294 tweets |
| **Periodo** | 2023 |
| **Etiquetado** | Sí (`good`, `bad`, `neutral`) |
| **Tamaño del archivo** | 33.6 MB |
| **URL** | [kaggle.com/datasets/charunisa/chatgpt-sentiment-analysis] |

**Columnas:**
- `Unnamed: 0` — índice
- `tweets` — texto del tweet
- `labels` — etiqueta de sentimiento

**Justificación:**
- **Ground truth:** Permite **validar** los modelos de sentimiento (VADER, TextBlob).
- **Volumen significativo:** 219k tweets con etiquetas manuales/automáticas.
- **Complementario:** Aunque no coincide exactamente con el corpus principal, sirve como benchmark.

**Limitación:** No se llegó a explotar completamente en este análisis por priorización de tiempo. **Recomendación futura:** usarlo para validar y calibrar los umbrales de clasificación.

---

### 3.3 Corpus geográfico: `ai_tweet.csv`

| Atributo | Valor |
|---------|-------|
| **Origen** | Kaggle (fuente original desconocida) |
| **Volumen** | 5,002 tweets |
| **Periodo** | Abril 2023 |
| **Metadata** | Incluye `location` |
| **Tamaño del archivo** | 1.4 MB |

**Columnas:**
- `Unnamed: 0` — índice
- `date` — timestamp
- `username` — autor
- `location` — ubicación geográfica del usuario
- `tweets` — texto
- `likes` — likes

**Justificación:**
- **Análisis geográfico:** Único corpus con `location`.
- **Volumen pequeño:** 5k tweets, útil para análisis exploratorio.
- **Diversidad:** 150+ ubicaciones únicas (NY, Australia, India, UK, etc.).

**Limitación:** No se integró en el análisis principal por diferencias de esquema. **Recomendación futura:** hacer un análisis geográfico dedicado.

---

## 4. Criterios de selección

Las fuentes se seleccionaron según **5 criterios ponderados**:

| Criterio | Peso | Descripción |
|----------|------|-------------|
| **Volumen** | 25% | ≥ 10,000 tweets por fuente |
| **Relevancia temática** | 25% | Contenido explícito sobre IA/ChatGPT |
| **Metadata útil** | 20% | Engagement, fecha, ubicación |
| **Facilidad de acceso** | 15% | Sin API paga, sin login |
| **Licencia** | 15% | Pública o CC-BY |

**Evaluación de las 3 fuentes seleccionadas:**

| Fuente | Volumen | Relevancia | Metadata | Acceso | Licencia | **Score** |
|--------|---------|-----------|----------|--------|----------|-----------|
| `Twitter Jan Mar.csv` | 10/10 | 10/10 | 9/10 | 10/10 | 10/10 | **9.75** |
| `sentiment/file.csv` | 9/10 | 8/10 | 3/10 | 10/10 | 10/10 | **7.85** |
| `ai_tweet.csv` | 4/10 | 8/10 | 8/10 | 10/10 | 10/10 | **7.30** |

---

## 5. Proceso de extracción

### 5.1 Descarga

Los 3 datasets se descargaron manualmente de Kaggle y se colocaron en `data/raw/tweets/`.

### 5.2 Validación inicial

```python
# Verificar integridad
assert df_principal.shape == (500036, 6), "Shape inesperado"
assert df_principal["content"].notna().all(), "Contenido nulo"
assert df_principal["date"].notna().all(), "Fecha nula"
```


```text
5.3 Análisis de calidad
Verificación	Resultado
Encoding	UTF-8 con fallback a latin-1
Nulos	< 0.01% del total
Duplicados	< 0.5% del total (eliminados)
Idioma	99.77% inglés, 0.23% español
Longitud media	167 caracteres

5.4 Documentación

Cada fuente se documentó con:

Origen (URL)

Volumen (filas × columnas)

Esquema (nombres y tipos de columna)

Cobertura temporal

Limitaciones conocidas


6. Consideraciones éticas y legales
6.1 Privacidad
Los datasets de Kaggle ya están anonimizados por los autores originales.

Los username son públicos en Twitter.

No se procesaron datos personales identificables (DNI, teléfono, email).

6.2 Uso permitido
Licencia: CC-BY (atribución requerida)

Uso: Análisis académico/educativo

No uso: Redistribución comercial

6.3 Cumplimiento GDPR
Los datos son públicos (tweets publicados en Twitter)

No hay datos sensibles (salud, orientación, religión)

No hay menores (política de Twitter: +13 años)

Derecho al olvido: si un usuario lo solicita, se puede excluir manualmente

7. Limitaciones de las fuentes
7.1 Twitter Jan Mar.csv
Limitación	Impacto	Mitigación
Solo 3 meses	No captura evolución anual	Ampliar corpus en futuro
Solo inglés	Análisis bilingüe marginal	Adquirir corpus hispano
Sin interacciones	Red limitada a co-ocurrencia	Twitter API paga
Sin ubicación	Sin análisis geográfico	Complementar con ai_tweet.csv
7.2 sentiment/file.csv
Limitación	Impacto	Mitigación
Etiquetado automático	Precisión desconocida	Validación manual en muestra
No coincide temporal	No es comparable 1:1	Usar solo como benchmark
7.3 ai_tweet.csv
Limitación	Impacto	Mitigación
Volumen bajo	No representativo	Usar solo para análisis exploratorio
Abril 2023	Fuera de la ventana principal	Análisis separado
location self-reported	Sesgo del usuario	Filtrar ubicaciones válidas
8. Comparativa con alternativas
8.1 ¿Por qué Kaggle y no scraping en vivo?
Aspecto	Kaggle	Scraping/API
Coste	Gratis	$100-5000/mes
Tiempo de setup	Minutos	Horas/días
Rate limits	Ninguno	Severos
Reproducibilidad	Alta	Baja (cambia cada hora)
Volumen	500k+	Limitado por API
Actualización	Manual	Automática
Conclusión: Para un reto académico con tiempo limitado, Kaggle es la elección pragmática.

8.2 ¿Por qué no Reddit?
Aspecto	Twitter	Reddit
Volumen	🔥🔥🔥	🔥🔥
Formato	Plano	Comentarios anidados
Idioma	Multi	Predominantemente inglés
Sesgo	Masivo	Técnico
Acceso	API cara	API pública
Conclusión: Reddit sería un complemento excelente para análisis de discurso técnico profundo, pero no como fuente principal.

9. Conclusiones
La combinación elegida (Kaggle principal + complementarios) ofrece el mejor balance coste/beneficio para este reto.

La limitación principal (sesgo temporal por muestreo) es un artefacto del pipeline, no de las fuentes — se corrige con un muestreo aleatorio.

El corpus es suficientemente rico para extraer insights significativos sobre el discurso IA en marzo 2023.

Ampliaciones futuras (más datasets, más idiomas, más periodos) mejorarían la robustez del análisis.

La transparencia documental (licencia, origen, limitaciones) es parte integral de un análisis ético y replicable.

10. Anexos
10.1 Enlaces a las fuentes originales
ChatGPT Tweets Jan-Mar 2023

ChatGPT Sentiment Analysis

AI Tweet Dataset (referencia específica del autor)

10.2 Estructura de data/raw/tweets/
text
data/raw/tweets/
├── ai_tweet.csv              (1.4 MB, 5,002 filas)
├── Twitter Jan Mar.csv       (111.6 MB, 500,036 filas)
└── sentiment/
    └── file.csv              (33.6 MB, 219,294 filas)
10.3 Script de validación
python
def validar_fuente(ruta):
    """Valida la integridad de una fuente."""
    df = pd.read_csv(ruta)
    print(f"📊 {ruta.name}")
    print(f"   Shape: {df.shape}")
    print(f"   Nulos: {df.isnull().sum().sum():,}")
    print(f"   Columnas: {list(df.columns)}")
    return df

# Ejecutar
validar_fuente("data/raw/tweets/Twitter Jan Mar.csv")
validar_fuente("data/raw/tweets/sentiment/file.csv")
validar_fuente("data/raw/tweets/ai_tweet.csv")




```