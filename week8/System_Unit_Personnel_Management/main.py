from fastapi import FastAPI
import uvicorn 
from utils import IO
from utils import helper

FILE_NAME = "soldiers.json"

app = FastAPI()


@app.get("/soldiers")
def get_list_soldiers():
    return IO.get_all_soldiers(FILE_NAME)


@app.get("/soldiers/{id}")
def get_soldier(id:int):
    return IO.get_the_soldier(FILE_NAME,id)



@app.post("/soldiers")
def create_soldier(body:dict):
    IO.add_soldier(FILE_NAME, body)


