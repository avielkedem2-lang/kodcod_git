import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s | %(asctime)s | %(message)s')
steam_handler = logging.StreamHandler()
steam_handler.setFormatter(formatter)


file_handler = logging.FileHandler("system.log", encoding="utf=8")
file_handler.setFormatter(formatter)

logger.addHandler(steam_handler)
logger.addHandler(file_handler)