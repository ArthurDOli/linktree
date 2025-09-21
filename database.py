from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models import Base, db

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db)

def getSession():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()