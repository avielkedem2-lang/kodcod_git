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
    return IO.add_soldier(FILE_NAME, body)


@app.put("/soldiers/{id}")
def updete_soldier(body:dict, id:int):
    return IO.updete_soldier_to_json(FILE_NAME, body, id)



@app.delete("/soldiers/{id}")
def delete_soldier(id:int):
    return IO.delete_a_soldier(FILE_NAME, id)


