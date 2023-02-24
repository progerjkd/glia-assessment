from datetime import datetime
from pydantic import BaseModel

class Audit(BaseModel):
    id: int
    timestamp: datetime
    url: str
    payload: str
    status: int
    duration: float

    class Config:
        orm_mode = True
