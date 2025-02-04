# schemas.py
from pydantic import BaseModel
import datetime

class SourceCreate(BaseModel):
    name: str
    url: str
    country: str
    year: int
    
class Source(BaseModel):
    id: int
    name: str
    url: str
    country: str
    year: int
    created_at: datetime.datetime

    class Config:
        from_attributes = True