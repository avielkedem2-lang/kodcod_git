from fastapi import FastAPI
import uvicorn 
from utils import IO
from utils import helper

FILE_NAME = "soldiers.json"

app = FastAPI()


@app.get("/soldiers")
def get_list_soldiers():
    return IO.get_all_soldiers(FILE_NAME)


@app.post("/soldiers")
def create_soldier(body:dict):
    IO.add_soldier(FILE_NAME, body)