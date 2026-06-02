from fastapi import FastAPI
import uvicorn 
import utils

FILE_NAME = "soldiers.json"

app = FastAPI()


@app.get("/soldiers")
def get_list_soldiers():
    return utils.IO.get_all_soldiers(FILE_NAME)