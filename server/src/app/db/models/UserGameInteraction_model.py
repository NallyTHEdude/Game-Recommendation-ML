from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from pgvector.sqlalchemy import Vector
from db import Base



class UserGameInteraction(Base):
    __tablename__ = "user_game_interactions"

    id = Column(String, primary_key=True)

    user_id = Column(String, ForeignKey("users.id"))
    game_id = Column(String, ForeignKey("games.id"))

    action_performed = Column(String)  # can switch to Enum if needed
    timestamp = Column(DateTime)

    user = relationship("User", back_populates="interactions")
    game = relationship("Game", back_populates="interactions")