from _core import config
from utils import logger

if __name__ == "__main__":
    print("Starting server with the following configuration:")
    print(config.DATABASE_URL)
    # Here you would typically start your server, e.g., using Flask or FastAPI
    # For example:
    # from fastapi import FastAPI
    # app = FastAPI()
    # ... define your routes and logic ...
    # uvicorn.run(app, host=config['SERVER_HOST'], port=config['PORT'])