from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# SQL DataBase
# from sqlalchemy import Column, Integer, String, create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# NoSQL DataBase -> MongoDB
# from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='templates')
# NoSQL DataBase -> MongoDB
# client = AsyncIOMotorClient('mongodb://127.0.0.1:27017')
# db = client["myfirstdatabaseinfastapi"]

# SQL DataBase
# engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(bind=engine)
# Base = declarative_base()

@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse('index.html', {request:request})