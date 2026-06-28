"""
CareerPilot AI

Application Class

Author: Vijayan
"""

from config.settings import settings
from utils.logger import logger
from utils.startup_validator import StartupValidator


class CareerPilotApplication:
    """
    Main Application Class
    """

    def __init__(self):

        logger.info("Creating CareerPilot Application...")

    def start(self):

        logger.info("=" * 60)
        logger.info(f"{settings.APP_NAME} - Version {settings.VERSION}")
        logger.info("=" * 60)

        StartupValidator.validate_project_structure()

        logger.info(f"Python Version      : {settings.PYTHON_VERSION}")
        logger.info(f"Operating System    : {settings.OPERATING_SYSTEM}")
        logger.info(f"Project Folder      : {settings.PROJECT_ROOT}")

        logger.success("CareerPilot AI Started Successfully")