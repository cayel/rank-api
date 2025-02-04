# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Récupérer les variables d'environnement
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
ENVIRONMENT = os.getenv("ENVIRONMENT")


SQLALCHEMY_DATABASE_URL = f"postgresql://postgres:{DATABASE_PASSWORD}@db.jsckbqjrbzxabhtplqod.supabase.co:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()