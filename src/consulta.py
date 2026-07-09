from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain
)

from langchain_classic.chains.retrieval import (
    create_retrieval_chain
)

from llm import llm
from prompt import obtener_prompt
from vectorstorage import vectorstore


def respuesta(pregunta: str) -> str:


    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "score_threshold": 0.4,
            "k": 4
        }
    )

    chain = create_stuff_documents_chain(
        llm,
        obtener_prompt()
    )

    rag = create_retrieval_chain(
        retriever,
        chain
    )

    resultado = rag.invoke(
        {"input": pregunta}
    )

    return resultado["answer"]