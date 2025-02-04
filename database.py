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
SQL_ALCHEMY_DATABASE= os.getenv("SQL_ALCHEMY_DATABASE")

engine = create_engine(SQL_ALCHEMY_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()