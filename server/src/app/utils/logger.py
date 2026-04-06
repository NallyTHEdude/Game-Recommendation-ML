from loguru import logger
import sys
import os
from pathlib import Path
import json

# Define log directory and file
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = LOG_DIR / "app.log"

# Remove default logger configuration
logger.remove()

# Add console logging with dynamic level
logger.add(sys.stderr, level=os.getenv("LOG_LEVEL", "DEBUG"), format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>")

# Add file logging with rotation and retention policies
logger.add(
    LOG_FILE,
    rotation="10 MB",  # Rotate log file after 10 MB
    retention="10 days",  # Keep logs for 10 days
    compression="zip",  # Compress rotated logs
    level="INFO",  # File logging level
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{function}:{line} - {message}"
)

logger.bind(user_id="USR-1243", doc_id="DOC-2348").debug("Processing document")
