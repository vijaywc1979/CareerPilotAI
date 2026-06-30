from pathlib import Path

from infrastructure.parsers.resume_parser import ResumeParser
from utils.logger import logger


class ResumeAgent:

    def __init__(self):

        self.parser = ResumeParser()

    def load_resume(self, resume_path: Path) -> str:

        logger.info("Loading Resume...")

        text = self.parser.parse(resume_path)

        logger.success("Resume Loaded Successfully")

        return text