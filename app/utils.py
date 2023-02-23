from contextlib import contextmanager
from .database import Audit, SessionLocal

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_log(n: int):
    with get_db() as db:
        return db.query(Audit).order_by(Audit.timestamp.desc()).limit(n)


def add_entry(**kwargs):
    log = Audit(**kwargs)
    with get_db() as db:
        db.add(log)
        db.commit()
