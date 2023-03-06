from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from config.database import  engine, Base
from middlewares.error_handler import ErrorHandler
from middlewares.jwt_beater import JWTBearer
from routers.movies import movie_router
from routers.user import user_router

app = FastAPI()

app.title = "Mi Api"
app.version = "0.0.2"


app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('<h1>Hello</h1>')
