from sqlalchemy import Boolean, Column, Integer, String

from .database import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String, unique=True, index=True)
    is_done = Column(Boolean, default=False)