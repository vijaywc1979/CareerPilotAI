from pathlib import Path

from docx import Document
from pypdf import PdfReader

from infrastructure.parsers.base_parser import BaseParser
from utils.logger import logger


class ResumeParser(BaseParser):

    def parse(self, file_path: Path) -> str:

        suffix = file_path.suffix.lower()

        if suffix == ".docx":
            return self._parse_docx(file_path)

        elif suffix == ".pdf":
            return self._parse_pdf(file_path)

        raise ValueError(f"Unsupported file type: {suffix}")

    def _parse_docx(self, file_path: Path) -> str:

        logger.info(f"Reading DOCX: {file_path.name}")

        document = Document(file_path)

        paragraphs = [
            paragraph.text.strip()
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        return "\n".join(paragraphs)

    def _parse_pdf(self, file_path: Path) -> str:

        logger.info(f"Reading PDF: {file_path.name}")

        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)