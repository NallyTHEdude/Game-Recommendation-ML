from _core import config
from utils import logger
from db import connect_db, init_db

if __name__ == "__main__":
    init_db()
    database = connect_db()
    logger.info("Application started successfully.")