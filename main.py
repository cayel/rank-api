# main.py
from fastapi import FastAPI, Depends
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()
    
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Essayez de faire une requête simple pour vérifier la connexion à la base de données
        db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "details": str(e)}




