from logger_config import logger
def chicke_criteria(body:dict):
    try: 
        if len(body) == 3:
            if len(str(body["id"])) == 4 and isinstance(body["id"], int):
                if body["full_name"] != "" and body["full_name"].isalpha():
                    if body["role"] != "" and body["role"].isalpha():
                        logger.info("yes i did it")
                        return True
        return False
    except Exception as e:
        logger.exception(f"There is a problem with the dictionary they entered, {e}")



def chicke_id(id):
    if len(str(id)) == 4 and isinstance(id, int):
        return True
    logger.error("The number less than or greater than 4 digits or is it not a digit!")
    return False