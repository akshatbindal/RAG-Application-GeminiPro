from dotenv import load_dotenv
load_dotenv()
import os
from typing import Iterable, Tuple
import google.generativeai as genai
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
from .utils import load_pdf, split_text

class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
        genai.configure(api_key=gemini_api_key)
        model = "models/embedding-001"
        title = "Custom query"
        return genai.embed_content(model=model,
                                   content=input,
                                   task_type="retrieval_document",
                                   title=title)["embedding"]

class ChromaDBManager:
    def __init__(self, path: str, name: str) -> None:
        self.path = path
        self.name = name
        self.chroma_client = chromadb.PersistentClient(path=self.path)
        self.db = None

    def create_chroma_db(self, documents: Iterable) -> Tuple[chromadb.Collection, str]:
        self.db = self.chroma_client.create_collection(name=self.name, embedding_function=GeminiEmbeddingFunction())

        for i, d in enumerate(documents):
            self.db.add(documents=d, ids=str(i))

        return self.db, self.name
    
    def load_chroma_collection(self) -> chromadb.Collection:
        self.db = self.chroma_client.get_collection(name=self.name, embedding_function=GeminiEmbeddingFunction())
        return self.db

if __name__=="__main__":
    pdftext = load_pdf(file_path="data\state_of_the_union.pdf")
    chunkedtext = split_text(pdftext)

    chroma_db_manager = ChromaDBManager(path="chromadb", name="rag_experiment")
    db, collection_name = chroma_db_manager.create_chroma_db( documents=chunkedtext)
    print("Success")