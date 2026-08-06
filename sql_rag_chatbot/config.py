import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.utilities import SQLDatabase
import pyodbc

load_dotenv()

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")


# Connect database variable
CONNECTION_STRING = (
    "mssql+pyodbc://sa:user123@HOMEPC,1433/Chinook"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&TrustServerCertificate=yes"
)
# Prompt
PROMPT="""
You are an expert SQL Server (T-SQL) developer.

Generate ONLY valid Microsoft SQL Server (T-SQL).

Rules:
- Use SQL Server syntax only.
- Use TOP instead of LIMIT.
- Do not use PostgreSQL or MySQL syntax.
- Do not use backticks (`).
- Return only the SQL query.
- Do not wrap the SQL in Markdown code fences.
- Do not include explanations.
Schema:{schema}
User question : {query}
Output (SQL only)
"""

# LLM model
LLM_MODEL_NAME="models/gemini-flash-latest"

# Embeddings
EMBEDDING_MODEL_NAME="gemini-embedding-001"
# 
VECTORE_STORE_PATH=os.path.join("data","faiss_index")

# Top result
TOP_K_RESULT=3

# Check if GIMINI_API_KEY is missing
def check_api_key():
    """ stop early with a clear message if required key is missing"""
    if not GEMINI_API_KEY:
        raise ValueError("Missing GIMINI_API_KEY  please added it to your .env file")