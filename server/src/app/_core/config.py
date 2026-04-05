import os 
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Settings():
    # Define all environment variables with default values
    ENVIRONMENT : str = os.getenv('ENVIRONMENT', 'development')
    PORT : int = int(os.getenv('PORT') or 3000)
    SERVER_HOST : str = os.getenv('SERVER_HOST', 'http://localhost')
    # if database does not exit, throw error 
    DATABASE_URL : str = os.getenv('DATABASE_URL') or TimeoutError("DATABASE_URL environment variable is required")

# export the config object
config = Settings()