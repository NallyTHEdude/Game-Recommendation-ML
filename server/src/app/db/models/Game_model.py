from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from db import Base


class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True)
    slug = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)

    release_date = Column(DateTime)
    background_image = Column(String)

    fetched_rating = Column(Float)
    user_rating = Column(Float)

    tags = Column(ARRAY(String))
    genre = Column(ARRAY(String))

    description = Column(String)
    playtime = Column(Float)

    embedding = Column(Vector(768))  # matches model "BAAI/bge-base-en-v1.5" output dimension

    interactions = relationship("UserGameInteraction", back_populates="game")