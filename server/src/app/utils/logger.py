import sys
import os
from pathlib import Path
from loguru import logger

LOG_DIR = Path("./logs")
LOG_DIR.mkdir(exist_ok=True)

valid_levels = {"TRACE", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
if log_level not in valid_levels:
    raise ValueError(f"Invalid LOG_LEVEL: {log_level}")

logger.remove()

# Console sink
logger.add(
    sys.stderr,
    level=log_level,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level}</level> | "
           "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    colorize=True,
    diagnose=False,   # Don't leak locals in prod
    catch=True,
)

# File sink — structured JSON for log aggregators
logger.add(
    LOG_DIR / "app.log",
    level="INFO",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    enqueue=True,      # Thread/async safe
    serialize=True,    # JSON lines output
    diagnose=False,
    catch=True,
)

# Dedicated error sink
logger.add(
    LOG_DIR / "error.log",
    level="ERROR",
    rotation="5 MB",
    retention="30 days",
    compression="zip",
    enqueue=True,
    serialize=True,
    diagnose=False,
    catch=True,
)