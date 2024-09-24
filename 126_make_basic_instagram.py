from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, session
from sqlalchemy import Column, Integer, String, Index
from pydantic import BaseModel


app = FastAPI()
engine = create_engine("sqlite:///Instagram.db", connect_args={'check_same_thread':False})
Base = declarative_base()
router = APIRouter(prefix="/user", tags=['user'])



class UserBase(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    __table_args__ = (Index('id_index', 'id'),) 

Base.metadata.create_all(engine)



sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    session = sessionlocal()
    try:
        yield session
    finally:
        session.close()

class User(BaseModel):
    username:str
    email:str
    password:str


class UserDisplay(BaseModel):
    username:str
    email:str
    class Config:
        orm_mode=True
def create_user(request: User, db: session):
    user = User(
        username=request.username,
        password=request.password, #hash
        email=request.email)
    
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.post("/", response_model=UserDisplay)
def create_user(request: User, db: session = Depends(get_db)):
    return create_user(request, db)


@app.get('/')
def home():
    return "First Page"