"""
CareerPilot AI Logger

Author: Vijayan
"""

from loguru import logger
import sys
from pathlib import Path

# Create logs folder if it doesn't exist
log_path = Path("logs")
log_path.mkdir(exist_ok=True)

# Remove default logger
logger.remove()

# Console logger
logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
           "<level>{level}</level> | "
           "<cyan>{message}</cyan>"
)

# File logger
logger.add(
    "logs/careerpilot.log",
    rotation="5 MB",
    retention="10 days",
    level="DEBUG",
    encoding="utf-8"
)

logger.info("Logger initialized successfully")