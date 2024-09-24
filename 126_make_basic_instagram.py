from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Index

app = FastAPI()
engine = create_engine("sqlite:///Instagram.db", connect_args={'check_same_thread':False})
Base = declarative_base()

class UserBase(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    __table_args__ = (Index('id_index', 'id'),) 

Base.metadata.create_all(engine)

@app.get('/')
def home():
    return "First Page"

sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    session = sessionlocal()
    try:
        yield session
    finally:
        session.close()