# import requests
import json


def get_all_soldiers(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        with open(filename, "w") as f:
            json.dump([], f)

