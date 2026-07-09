import platform
import sys

# En Linux usa pysqlite3 si está disponible.
# En Windows se utiliza sqlite3, que ya viene con Python.
if platform.system() != "Windows":
    try:
        __import__("pysqlite3")
        sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
    except ModuleNotFoundError:
        pass

import chromadb
from langchain_chroma import Chroma

from config import RUTA_VECTORDB
from embeddings import obtener_embeddings

persistent_client = chromadb.PersistentClient(
    path=str(RUTA_VECTORDB)
)

vectorstore = Chroma(
    client=persistent_client,
    collection_name="langchain",
    embedding_function=obtener_embeddings()
)
