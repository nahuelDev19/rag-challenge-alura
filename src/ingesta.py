from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import RUTA_DOCUMENTOS
from vectorstorage import vectorstore

loader = PyPDFDirectoryLoader(str(RUTA_DOCUMENTOS))
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(docs)

vectorstore.add_documents(chunks)

print(f"Se indexaron {len(chunks)} fragmentos.")