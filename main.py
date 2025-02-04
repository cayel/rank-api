# main.py
from fastapi import FastAPI, Depends, HTTPException
from database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import text
import models
import crud
import schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
    
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Essayez de faire une requête simple pour vérifier la connexion à la base de données
        db.execute(text("SELECT 1"))
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "details": str(e)}

@app.get("/sources/", response_model=list[schemas.Source])
def read_sources(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sources = crud.get_sources(db, skip=skip, limit=limit)
    return sources

@app.post("/sources/", response_model=schemas.Source)
def create_source(source: schemas.SourceCreate, db: Session = Depends(get_db)):
    return crud.create_source(db=db, name=source.name, url=source.url, country=source.country, year=source.year)


