# import requests
import json
from logger_config import logger
from .helper import *

def get_all_soldiers(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            logger.info("File read successfully")
            return json.load(file)
    except:
        with open(filename, "w") as f:
            logger.warning("open a new file")
            json.dump([], f)



def seve_to_json(filename, soldiers:list):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(soldiers, file, indent=2)
            logger.info("The save was successful")
    except Exception as e:
        logger.exception(f"Unable to save{e}")



def get_the_soldier(filename, id):
    if chicke_id(id):
        for milon in get_all_soldiers(filename):
            if milon["id"] == id:
                logger.info("The soldier was successfully found")
                return milon
        logger.error(f"There is no soldier with id {id}")
        return f"There is no soldier with id={id}"
    return "The number less than or greater than 4 digits or is it not a digit!"
    



def add_soldier(filename, body:dict):
    if chicke_criteria(body):
        soldiers = []
        for milon in get_all_soldiers(filename):
            soldiers.append(milon)
        soldiers.append(body)
        logger.info("Add soldier successfully")
        seve_to_json(filename, soldiers)
    else:
        logger.error("There is a problem with the dictionary they entered")



