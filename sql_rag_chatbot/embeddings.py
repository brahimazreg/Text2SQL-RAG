from sql_rag_chatbot import config
from langchain_community.vectorstores import FAISS
import os
from google import genai
from sql_rag_chatbot import config


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(
    api_key=config.GEMINI_API_KEY)

def embed_documents(texts):
    """ Convert schema documents into vectors   """
    response = client.models.embed_content(
        model=config.EMBEDDING_MODEL_NAME,
        contents=texts
    )

    return [
        item.values 
        for item in response.embeddings
    ]

def embed_query(question):
    """ Convert user question into a vector  """

    response = client.models.embed_content(
        model=config.EMBEDDING_MODEL_NAME,
        contents=question
    )

    return response.embeddings[0].values