"""
CareerPilot AI Configuration
Author: Vijayan
"""

from pathlib import Path
import platform
import sys


class Settings:
    """Application Settings"""

    APP_NAME = "CareerPilot AI"
    VERSION = "0.1"

    PROJECT_ROOT = Path(__file__).resolve().parent.parent

    PYTHON_VERSION = sys.version.split()[0]

    OPERATING_SYSTEM = platform.system()


settings = Settings()