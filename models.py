# models.py
from sqlalchemy import Column, Integer, String, DateTime
import datetime
from database import Base

class Source(Base):
    __tablename__ = "sources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    url = Column(String)
    country = Column(String)
    year = Column(Integer)
    created_at = Column(DateTime, default=datetime.datetime.now)
