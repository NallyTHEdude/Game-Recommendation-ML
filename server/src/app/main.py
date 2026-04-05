from _core import config
from utils import logger
from db import connect_db, init_db

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")
    database = connect_db()