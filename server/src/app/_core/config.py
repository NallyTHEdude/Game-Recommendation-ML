import os 
from dotenv import load_dotenv
from typing import Final, Optional

load_dotenv()

class Settings():
    _config_instance = None
    _initialized = False

    def __new__(cls):
        if cls._config_instance is None:
            cls._config_instance = super().__new__(cls)
        return cls._config_instance

    def __init__(self):
        if self._initialized:
            return
        # Define all environment variables with default values
        self.ENVIRONMENT : Final[str] = os.getenv('ENVIRONMENT', 'development')
        self.PORT : Final[int] = int(os.getenv('PORT') or 3000)
        self.SERVER_HOST : Final[str] = os.getenv('SERVER_HOST', 'http://localhost')

        # Handle database variables
        self.DATABASE_URL : Final[str] = os.getenv('DATABASE_URL')

        # Handle RAWG API variables
        self.RAWG_API_KEY : Final[Optional[str]] = os.getenv('RAWG_API_KEY')

        self._handle_errors()
        self._initialized = True
    
    def _handle_errors(self):
        if self.DATABASE_URL is None:
            raise KeyError("DATABASE_URL environment variable is required")
        if self.RAWG_API_KEY is None:
            raise KeyError("RAWG_API_KEY environment variable is required")


# export the config object
config = Settings()