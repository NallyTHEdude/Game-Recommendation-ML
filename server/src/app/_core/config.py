import os 
from dotenv import load_dotenv
from typing import Final, Optional
from dataclasses import dataclass

load_dotenv()

@dataclass(frozen=True)
class _Settings():
    # Define all environment variables with default values
    ENVIRONMENT : Final[str] = os.getenv('ENVIRONMENT', 'development')
    PORT : Final[int] = int(os.getenv('PORT') or 3000)
    SERVER_HOST : Final[str] = os.getenv('SERVER_HOST', 'http://localhost')

    # Handle database variables
    DATABASE_URL : Final[str] = os.getenv('DATABASE_URL')

    # Handle RAWG API variables
    RAWG_API_KEY : Final[Optional[str]] = os.getenv('RAWG_API_KEY')

    def __post_init__(self):
        if self.DATABASE_URL is None:
            raise KeyError("DATABASE_URL environment variable is required")
        if self.RAWG_API_KEY is None:
            raise KeyError("RAWG_API_KEY environment variable is required")


# export the config object
config = _Settings()