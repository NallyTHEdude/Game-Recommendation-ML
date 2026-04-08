from _core import config
from utils import logger
from db import connect_db, init_db
from ml import ml_models

if __name__ == "__main__":
    # uncomment in production to initialize the database on startup
    #init_db()
    database = connect_db()
    # embedding_model = ml_models.embedding_model
    # print(embedding_model.encode_passage(["action", "adventure"], ["RPG"], "An epic quest in a fantasy world."))
    logger.info("Application started successfully.")