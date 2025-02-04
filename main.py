# main.py
from fastapi import FastAPI, Depends, HTTPException
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

@app.get("/sources/")
def read_sources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        sources = db.execute(text("SELECT * FROM sources LIMIT :limit OFFSET :skip"), {'limit': limit, 'skip': skip}).fetchall()
        return {"sources": [dict(row) for row in sources]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


