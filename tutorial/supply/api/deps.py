from typing import Generator

from db.session import SessionLocal

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def get_current_user():
    pass

def get_current_active_user():
    pass