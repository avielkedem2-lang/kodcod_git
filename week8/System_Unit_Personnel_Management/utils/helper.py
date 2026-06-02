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