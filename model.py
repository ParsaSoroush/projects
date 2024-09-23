from database import Base

from sqlalchemy import Column, Integer, String

class UserBase(Base):
    __tablname__ = "user"
    id = Column(Integer ,Index=True, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)
