from dotenv import load_dotenv
load_dotenv()
import os
from src.RAG import ChromaDBManager
import google.generativeai as genai

def get_relevant_passage(query, db, n_results):
  passage = db.query(query_texts=[query], n_results=n_results)['documents'][0]
  return passage

def make_rag_prompt(query, relevant_passage):
  escaped = relevant_passage.replace("'", "").replace('"', "").replace("\n", " ")
  prompt = ("""You are a helpful and informative bot that answers questions using text from the reference passage included below. \
  Be sure to respond in a complete sentence, being comprehensive, including all relevant background information. \
  However, you are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and converstional tone. \
  If the passage is irrelevant to the answer, you may ignore it.
  QUESTION: '{query}'
  PASSAGE: '{relevant_passage}'

  ANSWER:
  """).format(query=query, relevant_passage=escaped)

  return prompt

def generate_answer(prompt):
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("Gemini API Key not provided. Please provide GEMINI_API_KEY as an environment variable")
    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

if __name__=="__main__":
   chroma_db_manager = ChromaDBManager(path="chromadb", name="rag_experiment")
   db = chroma_db_manager.load_chroma_collection()

   query = "what sanctions have been placed on Russia"

   relevant_text = get_relevant_passage(query,db,n_results=3)
   
   prompt = make_rag_prompt(query, relevant_passage="".join(relevant_text)) 

   answer = generate_answer(prompt)

   print(answer)