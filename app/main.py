import random
from typing import List
from fastapi import FastAPI, Request
from datetime import datetime, timedelta
from .schemas import Audit
from .utils import add_entry, get_entry
from . import database
from .database import engine

app = FastAPI()
database.Base.metadata.create_all(bind = engine)

@app.get("/")
async def root():
    return "Jumble API"

@app.get("/jumble/{word}")
async def jumble(word: str):
    random_word = random.sample(word, len(word))
    jumbled = ''.join(random_word)
    return {"jumbled": jumbled}

@app.get("/audit",response_model = List[Audit])
async def audit():
    return [Audit.from_orm(db_log) for db_log in get_entry(10)]

@app.middleware("http")
async def audit_request(request: Request, call_next):
    start = datetime.now()
    response = await call_next(request)
    end = datetime.now()

    ms = timedelta(milliseconds=1)

    add_entry(
        timestamp = start,
        url = str(request.url),
        payload = request.url.path,
        status = response.status_code,
        duration = (start - end) / ms,
    )
    return response
