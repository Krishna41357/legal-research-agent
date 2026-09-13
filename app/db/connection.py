import os 
# pyrefly: ignore [missing-import]
import psycopg
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL not set")

def get_connection():
    return psycopg.connect(DATABASE_URL)
