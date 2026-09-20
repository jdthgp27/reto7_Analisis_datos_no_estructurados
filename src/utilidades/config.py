"""
Configuración central del proyecto.
Aquí van rutas, parámetros y constantes reutilizables.
"""
from pathlib import Path

# --- Rutas base ---
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_RAW = BASE_DIR / "data" / "raw" / "tweets"
DATA_PROCESSED = BASE_DIR / "data" / "processed"
DATA_EXTERNAL = BASE_DIR / "data" / "external"
OUTPUTS_FIGURAS = BASE_DIR / "outputs" / "figuras"
OUTPUTS_REPORTES = BASE_DIR / "outputs" / "reportes"
OUTPUTS_MODELOS = BASE_DIR / "outputs" / "modelos"

# --- Parámetros de extracción ---
TEMA = "Inteligencia Artificial"
QUERY_TWITTER = "(AI OR \"artificial intelligence\" OR ChatGPT OR \"machine learning\") lang:es -is:retweet"
MAX_TWEETS = 5000

# --- Idiomas soportados ---
IDIOMAS = ["es", "en"]

# --- Parámetros de limpieza ---
MIN_LONGITUD_TEXTO = 3
IDIOMA_PRINCIPAL = "es"