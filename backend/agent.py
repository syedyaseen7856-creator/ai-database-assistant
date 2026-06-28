import os
from sqlalchemy import create_engine
from llama_index.core import SQLDatabase, Settings
from llama_index.core.query_engine import NLSQLTableQueryEngine

from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

from backend.config import GEMINI_API_KEY

# -----------------------
# DB PATH (FIXED)
# -----------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "company.db")

engine = create_engine(f"sqlite:///{DB_PATH}")
sql_database = SQLDatabase(engine)

# -----------------------
# AI MODELS
# -----------------------
Settings.llm = GoogleGenAI(
    model="gemini-2.5-flash",
    api_key=GEMINI_API_KEY,
)

Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# -----------------------
# QUERY ENGINE
# -----------------------
query_engine = NLSQLTableQueryEngine(
    sql_database=sql_database,
    llm=None 
)

print("✅ AI Agent Loaded Successfully!")
print("DB PATH USED:", DB_PATH)
print("🔥 API DB PATH:", DB_PATH)