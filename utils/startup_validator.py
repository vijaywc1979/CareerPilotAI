"""
CareerPilot AI
Startup Validator

Author: Vijayan
"""

from pathlib import Path

from utils.logger import logger


class StartupValidator:
    """
    Validates the application structure before startup.
    """

    REQUIRED_FOLDERS = [
        "agents",
        "config",
        "dashboard",
        "database",
        "logs",
        "models",
        "prompts",
        "resume",
        "services",
        "tests",
        "utils",
        "vectorstore"
    ]

    @classmethod
    def validate_project_structure(cls):

        logger.info("Checking project structure...")

        missing = []

        project_root = Path(__file__).resolve().parent.parent

        for folder in cls.REQUIRED_FOLDERS:

            folder_path = project_root / folder

            if folder_path.exists():

                logger.success(f"{folder:<15} ✓")

            else:

                logger.error(f"{folder:<15} ✗")

                missing.append(folder)

        if missing:

            logger.error("Project validation failed.")

            raise FileNotFoundError(
                f"Missing folders: {', '.join(missing)}"
            )

        logger.success("Project validation completed successfully.")