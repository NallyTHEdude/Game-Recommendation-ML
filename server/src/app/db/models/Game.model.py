from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from app.db import Base


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

    embedding = Column(Vector(1536))  # match your embedding model

    interactions = relationship("UserGameInteraction", back_populates="game")