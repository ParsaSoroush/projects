from fastapi import FastAPI
from model import Base
from database import engine

app = FastAPI()

Base.metadata.create_all(engine)

@app.get('/')
def home():
    return "First Page"