from langchain_openai import OpenAIEmbeddings
from config import MODELO_EMBEDDINGS

def obtener_embeddings():
    return OpenAIEmbeddings(
        model=MODELO_EMBEDDINGS
    )