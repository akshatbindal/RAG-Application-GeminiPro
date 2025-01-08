import streamlit as st
from typing import Iterable, Tuple
import google.generativeai as genai
from src.utils import load_pdf, split_text
from src.RAG import ChromaDBManager
from app import get_relevant_passage, make_rag_prompt, generate_answer

def create_chroma_db_from_pdf(file, name):
    pdftext = load_pdf(file)
    chunkedtext = split_text(pdftext)
    chroma_db_manager = ChromaDBManager(path="chromadb", name=name)
    db, collection_name = chroma_db_manager.create_chroma_db(documents=chunkedtext)
    return db, collection_name

# Streamlit UI
st.title("RAG-based Query Response System")

st.sidebar.title("Upload PDF and Create ChromaDB Vector")
uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type="pdf", key="file_uploader")
collection_name = st.sidebar.text_input("Enter a name for the ChromaDB collection", key="collection_name_input")

if st.sidebar.button("Create ChromaDB Vector", key="create_chroma_db_button"):
    if uploaded_file and collection_name:
        with st.spinner("Creating ChromaDB vector..."):
            db, collection_name = create_chroma_db_from_pdf(uploaded_file, collection_name)
            st.sidebar.success(f"ChromaDB vector created with name: {collection_name}")
    else:
        st.sidebar.error("Please upload a PDF file and provide a name for the collection.")

st.header("Query the ChromaDB Vector")
query = st.text_input("Enter your query:", key="query_input")

if st.button("Get Answer", key="get_answer_button"):
    if query and collection_name:
        chroma_db_manager = ChromaDBManager(path="chromadb", name=collection_name)
        db = chroma_db_manager.load_chroma_collection()
        
        with st.spinner("Retrieving relevant passage..."):
            relevant_text = get_relevant_passage(query, db, n_results=3)
            prompt = make_rag_prompt(query, relevant_passage="".join(relevant_text))
        
        with st.spinner("Generating answer..."):
            answer = generate_answer(prompt)
        
        st.success("Answer:")
        st.write(answer)
    else:
        st.error("Please enter a query and ensure a ChromaDB collection is created.")
