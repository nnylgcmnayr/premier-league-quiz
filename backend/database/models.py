from sqlalchemy import Column, Integer, String
from .database import Base

class Player(Base):
    __tablename__ = "players"

    player_id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    team_id = Column(Integer, index=True)
    team_name = Column(String(50), nullable=False)
    birthdate = Column(String(50), nullable=True)
    position_id = Column(String(20), nullable=True)
    position = Column(String(20), nullable=False)
    age = Column(Integer, nullable=False)