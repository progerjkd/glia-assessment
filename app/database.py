from sqlalchemy import Column, String, Integer, Float, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
import os

DB_USER=os.environ.get('DB_USER')
DB_PASSWORD=os.environ.get('DB_PASSWORD')
DB_HOST=os.environ.get('DB_HOST')
DB_NAME=os.environ.get('DB_NAME')

SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

if not database_exists(SQLALCHEMY_DATABASE_URL):
    create_database(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Audit(Base):
    __tablename__ = "audit"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    url = Column(String(100))
    payload = Column(String(100))
    status = Column(Integer)
    duration = Column(Float)

def create_db():
    Base.metadata.create_all(bind=engine)
