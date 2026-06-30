from pathlib import Path

from infrastructure.parsers.resume_parser import ResumeParser
from utils.logger import logger


class ResumeAgent:
    """
    Agent responsible for loading and parsing resumes.
    """

    def __init__(self) -> None:
        self.parser = ResumeParser()

    def load_resume(self, resume_path: Path) -> str:
        """
        Load and parse a resume.
        """

        logger.info("Loading Resume...")

        text = self.parser.parse(resume_path)

        logger.success("Resume Loaded Successfully")

        return text