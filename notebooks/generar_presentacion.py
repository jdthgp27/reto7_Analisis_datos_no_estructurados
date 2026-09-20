# ============================================
# Generador de Presentación PowerPoint
# Reto 7 — Análisis de Datos No Estructurados y Redes Sociales
# ============================================
import os
from pathlib import Path
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ============================================
# CONFIGURACIÓN
# ============================================
BASE_DIR = Path(r"C:\Users\jdthg\Documents\curso6BI\reto7_Analisis_datos_no_estructurados")
FIGURAS = BASE_DIR / "outputs" / "figuras"
DOCS = BASE_DIR / "docs"
RUTA_SALIDA = DOCS / "presentacion_reto7.pptx"

# Colores corporativos
COLOR_PRIMARIO = RGBColor(0x1F, 0x3A, 0x5F)
COLOR_SECUNDARIO = RGBColor(0x2E, 0x86, 0xAB)
COLOR_ACENTO = RGBColor(0xF7, 0x7F, 0x00)
COLOR_TEXTO = RGBColor(0x33, 0x33, 0x33)
COLOR_FONDO = RGBColor(0xF5, 0xF5, 0xF5)
COLOR_BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

# Dimensiones 16:9
ANCHO = Inches(13.333)
ALTO = Inches(7.5)

# ============================================
# HELPERS
# ============================================
def add_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def add_title_bar(slide, texto, color=COLOR_PRIMARIO):
    barra = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, ANCHO, Inches(1.1))
    barra.fill.solid()
    barra.fill.fore_color.rgb = color
    barra.line.fill.background()
    tf = barra.text_frame
    tf.margin_left = Inches(0.5)
    tf.margin_top = Inches(0.2)
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.text = texto
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLANCO
    p.alignment = PP_ALIGN.LEFT
    return barra

def add_text_box(slide, texto, left, top, width, height,
                 font_size=18, bold=False, color=COLOR_TEXTO,
                 align=PP_ALIGN.LEFT):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = texto
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.alignment = align
    return tb

def add_bullet_list(slide, items, left, top, width, height,
                    font_size=18, color=COLOR_TEXTO, spacing=Pt(6)):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    for i, item in enumerate(items):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = f"•  {item}"
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.space_after = spacing
    return tb

def add_footer(slide, numero, total):
    footer = slide.shapes.add_textbox(Inches(12), Inches(7.0), Inches(1.2), Inches(0.4))
    tf = footer.text_frame
    p = tf.paragraphs[0]
    p.text = f"{numero} / {total}"
    p.font.size = Pt(10)
    p.font.color.rgb = RGBColor(0x88, 0x88, 0x88)
    p.alignment = PP_ALIGN.RIGHT

def add_image_safe(slide, ruta_imagen, left, top, width=None, height=None):
    ruta_imagen = Path(ruta_imagen)
    if ruta_imagen.exists():
        if width and height:
            slide.shapes.add_picture(str(ruta_imagen), left, top, width, height)
        elif width:
            slide.shapes.add_picture(str(ruta_imagen), left, top, width=width)
        elif height:
            slide.shapes.add_picture(str(ruta_imagen), left, top, height=height)
        else:
            slide.shapes.add_picture(str(ruta_imagen), left, top)
        return True
    else:
        print(f"⚠️ No existe: {ruta_imagen}")
        return False

# ============================================
# CREAR PRESENTACIÓN
# ============================================
prs = Presentation()
prs.slide_width = ANCHO
prs.slide_height = ALTO

TOTAL_SLIDES = 17
slide_num = 0

# ============================================
# SLIDE 1 — Portada
# ============================================
slide_num += 1
slide = add_slide(prs)
bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, ANCHO, ALTO)
bg.fill.solid()
bg.fill.fore_color.rgb = COLOR_PRIMARIO
bg.line.fill.background()

add_text_box(slide, "Reto 7 — Análisis de Datos No Estructurados",
             Inches(1), Inches(2.0), Inches(11.3), Inches(1.2),
             font_size=42, bold=True, color=COLOR_BLANCO, align=PP_ALIGN.CENTER)

add_text_box(slide, "Análisis NLP de 100,000 tweets sobre inteligencia artificial",
             Inches(1), Inches(3.3), Inches(11.3), Inches(0.8),
             font_size=22, color=COLOR_ACENTO, align=PP_ALIGN.CENTER)

add_text_box(slide, "[Tu Nombre]  ·  Curso 6 — Business Intelligence y Big Data",
             Inches(1), Inches(5.0), Inches(11.3), Inches(0.6),
             font_size=16, color=COLOR_BLANCO, align=PP_ALIGN.CENTER)

add_text_box(slide, "[Fecha de entrega]",
             Inches(1), Inches(5.6), Inches(11.3), Inches(0.6),
             font_size=14, color=COLOR_BLANCO, align=PP_ALIGN.CENTER)

# ============================================
# SLIDE 2 — Índice
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Contenido de la presentación")
add_bullet_list(slide, [
    "1.  Contexto y objetivos del reto",
    "2.  Fuentes de datos utilizadas",
    "3.  Metodología: pipeline técnico",
    "4.  Tratamiento y preparación de los datos",
    "5.  Análisis exploratorio y visualización",
    "6.  Análisis de sentimiento (NLP)",
    "7.  Extracción de entidades (NER) y tópicos (LDA)",
    "8.  Análisis de redes de co-ocurrencia",
    "9.  Dificultades encontradas",
    "10. Resultados obtenidos e insights",
    "11. Recomendaciones estratégicas",
    "12. Conclusiones y próximos pasos",
], Inches(1), Inches(1.6), Inches(11.3), Inches(5.5), font_size=18, spacing=Pt(8))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 3 — Contexto y objetivos
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Contexto y objetivos")

add_text_box(slide, "Contexto", Inches(0.7), Inches(1.4), Inches(6), Inches(0.5),
             font_size=22, bold=True, color=COLOR_SECUNDARIO)
add_bullet_list(slide, [
    "ChatGPT y GPT-4 marcaron un punto de inflexión en la percepción pública de la IA (marzo 2023).",
    "Twitter/X se convirtió en el principal foro de discusión masiva.",
    "Necesidad de entender: ¿qué se dice? ¿con qué sentimiento? ¿quiénes lideran el discurso?",
], Inches(0.7), Inches(1.9), Inches(6), Inches(3.5), font_size=15, spacing=Pt(8))

add_text_box(slide, "Objetivos", Inches(7.2), Inches(1.4), Inches(5.5), Inches(0.5),
             font_size=22, bold=True, color=COLOR_SECUNDARIO)
add_bullet_list(slide, [
    "Extraer y preparar un corpus de tweets sobre IA.",
    "Cuantificar el sentimiento público.",
    "Identificar entidades mencionadas.",
    "Descubrir temas latentes con LDA.",
    "Analizar la red de co-ocurrencia de entidades.",
    "Traducir los hallazgos en recomendaciones.",
], Inches(7.2), Inches(1.9), Inches(5.5), Inches(3.5), font_size=15, spacing=Pt(6))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 4 — Fuentes de datos
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Fuentes de datos")

add_text_box(slide, "Datasets utilizados (Kaggle)", Inches(0.7), Inches(1.4), Inches(12), Inches(0.5),
             font_size=22, bold=True, color=COLOR_SECUNDARIO)
add_bullet_list(slide, [
    "Twitter Jan Mar.csv — 500,036 tweets sobre ChatGPT (khalidryder777).",
    "sentiment/file.csv — 219,294 tweets etiquetados (charunisa).",
    "ai_tweet.csv — 5,002 tweets con ubicación geográfica.",
], Inches(0.7), Inches(2.0), Inches(12), Inches(2.5), font_size=17, spacing=Pt(10))

add_text_box(slide, "Criterios de selección", Inches(0.7), Inches(4.4), Inches(12), Inches(0.5),
             font_size=22, bold=True, color=COLOR_SECUNDARIO)
add_bullet_list(slide, [
    "✓ Volumen suficiente (≥ 10,000 tweets por fuente).",
    "✓ Relevancia temática explícita sobre IA/ChatGPT.",
    "✓ Metadata útil (engagement, fecha, ubicación).",
    "✓ Acceso libre y licencia pública (CC-BY).",
], Inches(0.7), Inches(5.0), Inches(12), Inches(2.0), font_size=15, spacing=Pt(6))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 5 — Metodología: pipeline
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Metodología: pipeline técnico")

fases = [
    ("01", "Extracción", "Carga CSV\nValidación"),
    ("02", "Preparación", "Limpieza\nTokenización"),
    ("03", "EDA", "Análisis\nexploratorio"),
    ("04", "NLP", "VADER\nTextBlob"),
    ("05", "NER + LDA", "SpaCy\nscikit-learn"),
    ("06", "Redes", "NetworkX\nLouvain"),
    ("07", "Informe", "Insights\nRecomendaciones"),
]

x_start = Inches(0.5)
y_top = Inches(2.5)
ancho_fase = Inches(1.7)
alto_fase = Inches(2.5)
espacio = Inches(0.15)

for i, (num, titulo, desc) in enumerate(fases):
    x = x_start + i * (ancho_fase + espacio)
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y_top, ancho_fase, alto_fase)
    shape.fill.solid()
    shape.fill.fore_color.rgb = COLOR_SECUNDARIO if i % 2 == 0 else COLOR_PRIMARIO
    shape.line.fill.background()

    tf = shape.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tf.paragraphs[0]
    p.text = num
    p.font.size = Pt(24)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACENTO
    p.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = titulo
    p2.font.size = Pt(14)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_BLANCO
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf.add_paragraph()
    p3.text = desc
    p3.font.size = Pt(10)
    p3.font.color.rgb = COLOR_BLANCO
    p3.alignment = PP_ALIGN.CENTER

    if i < len(fases) - 1:
        flecha = slide.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW,
            x + ancho_fase, y_top + alto_fase/2 - Inches(0.15), espacio, Inches(0.3))
        flecha.fill.solid()
        flecha.fill.fore_color.rgb = COLOR_ACENTO
        flecha.line.fill.background()

add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 6 — Tratamiento de datos (I)
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Tratamiento de los datos (I)")

add_text_box(slide, "Limpieza aplicada al texto", Inches(0.7), Inches(1.4), Inches(12), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "Normalización: conversión a minúsculas.",
    "Eliminación de URLs (https://t.co/...).",
    "Eliminación de menciones (@usuario).",
    "Hashtags: se preserva el texto (#ChatGPT → chatgpt).",
    "Eliminación de emojis (regex unicode).",
    "Eliminación de números y símbolos especiales.",
    "Normalización de espacios múltiples.",
], Inches(0.7), Inches(2.0), Inches(12), Inches(4.0), font_size=16, spacing=Pt(8))

caja = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE,
    Inches(0.7), Inches(5.8), Inches(12), Inches(1.2))
caja.fill.solid()
caja.fill.fore_color.rgb = RGBColor(0xE8, 0xF4, 0xF8)
caja.line.color.rgb = COLOR_SECUNDARIO

tf = caja.text_frame
tf.margin_left = Inches(0.3)
tf.vertical_anchor = MSO_ANCHOR.MIDDLE
p = tf.paragraphs[0]
p.text = "Objetivo: reducir el ruido y quedarnos solo con el contenido semántico relevante para el análisis de sentimiento y NLP."
p.font.size = Pt(14)
p.font.italic = True
p.font.color.rgb = COLOR_PRIMARIO

add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 7 — Tratamiento de datos (II)
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Tratamiento de los datos (II)")

add_text_box(slide, "Tokenización y lematización", Inches(0.7), Inches(1.4), Inches(12), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "Stopwords combinadas: inglés (198) + español (313) + custom (52) = 553.",
    "Excluidas de stopwords: 'chatgpt', 'openai', 'gpt' (términos clave del dominio).",
    "Tokenización simple por split + filtrado de stopwords.",
    "Lematización con SpaCy bilingüe (en_core_web_sm + es_core_news_sm).",
    "Detección de idioma por heurística (caracteres latinos + palabras funcionales).",
], Inches(0.7), Inches(2.0), Inches(12), Inches(3.5), font_size=16, spacing=Pt(8))

add_text_box(slide, "Estadísticas del corpus procesado", Inches(0.7), Inches(5.3), Inches(12), Inches(0.5),
             font_size=18, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "100,000 tweets procesados  ·  63,418 usuarios únicos.",
    "Idioma: 99.77% inglés  ·  0.23% español.",
    "Longitud media del texto limpio: 134 caracteres.",
], Inches(0.7), Inches(5.8), Inches(12), Inches(1.5), font_size=15, spacing=Pt(4))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 8 — Análisis exploratorio
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Análisis exploratorio (EDA)")

add_image_safe(slide, FIGURAS / "03_top_30_palabras.png",
               Inches(0.5), Inches(1.4), width=Inches(6))
add_image_safe(slide, FIGURAS / "03_wordcloud_chatgpt.png",
               Inches(6.8), Inches(1.4), width=Inches(6))

add_text_box(slide, "Términos dominantes: chatgpt, gpt, google, microsoft, ai, nft, crypto.",
             Inches(0.5), Inches(6.8), Inches(12), Inches(0.5),
             font_size=14, color=COLOR_TEXTO, align=PP_ALIGN.CENTER)
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 9 — Análisis de sentimiento
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Análisis de sentimiento (NLP)")

add_image_safe(slide, FIGURAS / "04_distribucion_sentimiento.png",
               Inches(0.5), Inches(1.4), width=Inches(7.5))

add_text_box(slide, "Resultados VADER", Inches(8.3), Inches(1.5), Inches(4.8), Inches(0.5),
             font_size=18, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "🟢 Positivo: 53.26% (53,260 tweets)",
    "⚪ Neutral: 30.68% (30,678 tweets)",
    "🔴 Negativo: 16.06% (16,062 tweets)",
    "",
    "Compound medio: +0.2174",
    "Desviación estándar: 0.4081",
    "",
    "Engagement:",
    "  · Positivos: 9.49 likes  ·  1.96 RT",
    "  · Negativos: 7.23 likes  ·  1.19 RT",
    "  · Neutrales: 5.82 likes  ·  0.90 RT",
], Inches(8.3), Inches(2.0), Inches(4.8), Inches(4.5), font_size=13, spacing=Pt(3))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 10 — NER y LDA
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Extracción de entidades (NER) y tópicos (LDA)")

add_text_box(slide, "Top entidades detectadas", Inches(0.5), Inches(1.4), Inches(6.5), Inches(0.5),
             font_size=18, bold=True, color=COLOR_SECUNDARIO)
add_bullet_list(slide, [
    "🏢 gpt (ORG): 33,279 menciones",
    "🏢 google (ORG): 1,389",
    "🏢 microsoft (ORG): 1,079",
    "👤 sam altman (PERSON): 381",
    "📦 google s bard (PRODUCT): 93",
    "",
    "Total: 64,268 entidades (10,718 únicas).",
    "Tipos: ORG, PERSON, GPE, PRODUCT, EVENT, NORP, MONEY, WORK_OF_ART.",
], Inches(0.5), Inches(2.0), Inches(6.5), Inches(4.5), font_size=14, spacing=Pt(4))

add_text_box(slide, "Temas LDA detectados (8)", Inches(7.3), Inches(1.4), Inches(5.5), Inches(0.5),
             font_size=18, bold=True, color=COLOR_SECUNDARIO)
add_bullet_list(slide, [
    "Tema 0: IA generativa y escritura",
    "Tema 1: Herramientas y chatbots",
    "Tema 2: Cripto + IA (nicho)",
    "Tema 3: Futuro y capacidades",
    "Tema 4: Uso general y preguntas",
    "Tema 5: Microsoft/Bing + marketing",
    "Tema 6: Aprendizaje y juegos",
    "Tema 7: Google Bard y educación",
], Inches(7.3), Inches(2.0), Inches(5.5), Inches(4.5), font_size=14, spacing=Pt(6))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 11 — Red de co-ocurrencia
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Análisis de redes de co-ocurrencia")

add_image_safe(slide, FIGURAS / "06_red_entidades.png",
               Inches(0.5), Inches(1.4), width=Inches(7.5))

add_text_box(slide, "Características", Inches(8.3), Inches(1.5), Inches(4.8), Inches(0.5),
             font_size=18, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "Nodos: 77",
    "Aristas: 254",
    "Comunidades: 4 (Louvain)",
    "",
    "Top hubs:",
    "  1. gpt (grado 2,344)",
    "  2. google (grado 521)",
    "  3. microsoft (grado 447)",
    "  4. sam altman (grado 206)",
    "",
    "Comunidades:",
    "  · Núcleo OpenAI/ChatGPT",
    "  · Eje Google-Microsoft",
    "  · Política y personalidades",
    "  · Medios y academia",
], Inches(8.3), Inches(2.0), Inches(4.8), Inches(5.0), font_size=12, spacing=Pt(2))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 12 — Dificultades (I)
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Dificultades encontradas (I)", color=RGBColor(0xB0, 0x30, 0x30))

add_text_box(slide, "Retos técnicos", Inches(0.7), Inches(1.4), Inches(12), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "📉 Sesgo temporal severo: el muestreo df.head(100k) sobre CSV ordenado descendentemente limitó el análisis a solo 14 días (16-29 marzo 2023), no los 3 meses originales.",
    "🔤 Lematización bilingüe imperfecta: SpaCy es_core_news_sm lematizó incorrectamente términos ingleses (writtir, peoplir, datar, freir).",
    "🌐 Desequilibrio lingüístico extremo: 99.77% de los tweets en inglés, solo 0.23% en español → el pipeline bilingüe aportó poco valor real.",
    "🔍 Ruido en NER: falsos positivos por contracciones inglesas (don, doesn) y posesivos (google s). Fragmentos mal extraídos (gpt gpt).",
    "⏱️ Tiempos de procesamiento: procesar 100k tweets con SpaCy tardó ~8-10 minutos, condicionando la iteración rápida.",
], Inches(0.7), Inches(2.0), Inches(12), Inches(5.0), font_size=14, spacing=Pt(10))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 13 — Dificultades (II)
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Dificultades encontradas (II)", color=RGBColor(0xB0, 0x30, 0x30))

add_text_box(slide, "Retos metodológicos y conceptuales", Inches(0.7), Inches(1.4), Inches(12), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "📐 Red de tamaño modesto: con MIN_FREQ=20 solo quedaron 77 nodos, lo que limita la interpretabilidad estructural de la red.",
    "🔗 Co-ocurrencia ≠ interacción real: la red refleja proximidad temática, no influencia social (retweets, replies, menciones).",
    "✅ Sin ground truth específico: no se validó VADER/TextBlob contra etiquetas del corpus IA, aunque sí contra benchmarks genéricos.",
    "📊 Ruido temático: los tweets cripto/NFT se mezclaron con discurso IA, generando temas híbridos difíciles de separar.",
    "🎨 Falta de análisis multimodal: imágenes, vídeos y memes (muy relevantes en IA) quedaron fuera del análisis.",
    "🕒 Presupuesto de tiempo: el análisis exhaustivo de las 3 fases (NLP + NER + Redes) requirió priorizar y dejar validaciones para futuras iteraciones.",
], Inches(0.7), Inches(2.0), Inches(12), Inches(5.0), font_size=14, spacing=Pt(8))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 14 — Resultados obtenidos
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Resultados obtenidos e insights")

resultados = [
    ("53.26%", "Tweets positivos", "Sentimiento favorable dominante"),
    ("16.06%", "Tweets negativos", "Foco en ética y sesgos"),
    ("33,279", "Menciones de gpt", "Hub absoluto del discurso"),
    ("4", "Comunidades", "OpenAI · Google · Política · Medios"),
    ("8", "Temas LDA", "IA generativa, cripto, educación..."),
    ("+0.217", "Compound medio", "Sentimiento global positivo"),
]

x_start = Inches(0.4)
y_top = Inches(1.5)
ancho = Inches(2.0)
alto = Inches(2.3)
gap = Inches(0.15)

for i, (valor, titulo, desc) in enumerate(resultados):
    fila = i // 6
    columna = i % 6
    x = x_start + columna * (ancho + gap)
    y = y_top + fila * (alto + gap)

    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, x, y, ancho, alto)
    card.fill.solid()
    card.fill.fore_color.rgb = COLOR_PRIMARIO
    card.line.fill.background()

    tf = card.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE

    p = tf.paragraphs[0]
    p.text = valor
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACENTO
    p.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = titulo
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_BLANCO
    p2.alignment = PP_ALIGN.CENTER

    p3 = tf.add_paragraph()
    p3.text = desc
    p3.font.size = Pt(9)
    p3.font.color.rgb = RGBColor(0xCC, 0xCC, 0xCC)
    p3.alignment = PP_ALIGN.CENTER

add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 15 — Recomendaciones clave
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Recomendaciones estratégicas clave")

add_text_box(slide, "Prioridades identificadas (🔥 críticas)", Inches(0.7), Inches(1.4), Inches(12), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "🔥 1. Aprovechar la ventana positiva antes del ciclo crítico (6-12 meses).",
    "🔥 2. Co-ocurrir con ChatGPT para ganar visibilidad en el discurso IA.",
    "🔥 3. Priorizar integraciones con ChatGPT API frente a modelos propios.",
    "🔥 4. Atacar verticales específicas (legal, salud, educación) con baja competencia.",
    "🔥 5. Elegir 1-2 comunidades de la red y dominarlas, no intentar cubrir todo.",
    "",
    "⚡ 6. Evitar ruido cripto-IA si no es el core del negocio.",
    "⚡ 7. Explorar el mercado hispanohablante (desatendido).",
    "⚡ 8. Construir narrativa positiva pero no ingenua (70% beneficio / 20% desafíos / 10% visión).",
    "⚡ 9. Prepararse para la regulación (AI Act europea).",
    "⚡ 10. Industrializar el pipeline NLP para análisis continuo.",
], Inches(0.7), Inches(2.0), Inches(12), Inches(5.0), font_size=14, spacing=Pt(6))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 16 — Conclusiones
# ============================================
slide_num += 1
slide = add_slide(prs)
add_title_bar(slide, "Conclusiones y próximos pasos")

add_text_box(slide, "Conclusiones principales", Inches(0.7), Inches(1.4), Inches(6), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "El sentimiento público hacia la IA en marzo 2023 fue claramente positivo.",
    "ChatGPT/OpenAI domina el discurso de forma casi monopólica.",
    "La competencia OpenAI vs Google es el segundo eje discursivo.",
    "La comunidad cripto-IA es un nicho significativo pero minoritario.",
    "La red se estructura en 4 comunidades con ChatGPT como hub central.",
    "El análisis bilingüe fue marginal (99.77% inglés).",
], Inches(0.7), Inches(2.0), Inches(6), Inches(4.5), font_size=14, spacing=Pt(6))

add_text_box(slide, "Próximos pasos", Inches(7), Inches(1.4), Inches(6), Inches(0.5),
             font_size=20, bold=True, color=COLOR_SECUNDARIO)

add_bullet_list(slide, [
    "Corto plazo (1-3 meses):",
    "  · Corregir sesgo temporal con muestreo estratificado.",
    "  · Validar sentimiento contra ground truth.",
    "  · Industrializar pipeline a scripts reproducibles.",
    "",
    "Medio plazo (3-6 meses):",
    "  · Ampliar corpus a 500k tweets completos.",
    "  · Incorporar análisis de interacciones reales (retweets, replies).",
    "  · Migrar sentimiento a BERT/RoBERTa.",
    "",
    "Largo plazo (6-12 meses):",
    "  · Análisis multimodal (imágenes, videos).",
    "  · Dashboard de monitorización continua.",
], Inches(7), Inches(2.0), Inches(6), Inches(5.0), font_size=12, spacing=Pt(3))
add_footer(slide, slide_num, TOTAL_SLIDES)

# ============================================
# SLIDE 17 — Cierre
# ============================================
slide_num += 1
slide = add_slide(prs)

bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, ANCHO, ALTO)
bg.fill.solid()
bg.fill.fore_color.rgb = COLOR_PRIMARIO
bg.line.fill.background()

add_text_box(slide, "Gracias por su atención",
             Inches(1), Inches(2.5), Inches(11.3), Inches(1.2),
             font_size=48, bold=True, color=COLOR_BLANCO, align=PP_ALIGN.CENTER)

add_text_box(slide, "¿Preguntas?",
             Inches(1), Inches(3.8), Inches(11.3), Inches(0.8),
             font_size=28, color=COLOR_ACENTO, align=PP_ALIGN.CENTER)

add_text_box(slide, "[Tu Nombre]  ·  [Tu email]  ·  github.com/[Tu_Usuario]",
             Inches(1), Inches(5.5), Inches(11.3), Inches(0.6),
             font_size=14, color=COLOR_BLANCO, align=PP_ALIGN.CENTER)

# ============================================
# GUARDAR
# ============================================
RUTA_SALIDA.parent.mkdir(parents=True, exist_ok=True)
prs.save(str(RUTA_SALIDA))
print(f"✅ Presentación guardada: {RUTA_SALIDA}")
print(f"📊 Total diapositivas: {slide_num}")