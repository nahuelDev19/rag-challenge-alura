import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(override=True)

BASE_DIR = Path(__file__).resolve().parent.parent

OPENAI_API_KEY = os.getenv( "OPENAI_API_KEY")
RUTA_VECTORDB = BASE_DIR / "vectordb"
RUTA_DOCUMENTOS = BASE_DIR / "data"

MODELO_CHAT = "gpt-4o-mini"
MODELO_EMBEDDINGS = "text-embedding-3-small"


