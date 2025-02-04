from sqlalchemy.orm import Session
import models

def get_sources(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Source).offset(skip).limit(limit).all()

def create_source(db: Session, name: str, url: str, country: str, year: int):
    db_source = models.Source(name=name, url=url, country=country, year=year)
    db.add(db_source)
    db.commit()
    db.refresh(db_source)
    return db_source