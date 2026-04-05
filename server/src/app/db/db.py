from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from _core import config

DATABASE_URL = config.DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    )

Base = declarative_base()


def init_db():
    from db.models import Game, User, UserGameInteraction
    Base.metadata.create_all(bind=engine)

def connect_db():
    try:
        db = SessionLocal()
        print("Database connection established successfully.")
        return db
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        db.close()
        raise