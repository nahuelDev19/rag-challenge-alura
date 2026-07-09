from langchain_openai import ChatOpenAI
from config import MODELO_CHAT

llm = ChatOpenAI(
    model=MODELO_CHAT,
    temperature=0
)