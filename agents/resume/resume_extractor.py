import re

from domain.models.resume_profile import ResumeProfile


class ResumeExtractor:

    def extract(self, text: str) -> ResumeProfile:

        profile = ResumeProfile()

        profile.email = self.extract_email(text)

        profile.phone = self.extract_phone(text)

        return profile

    def extract_email(self, text: str) -> str:

        match = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        return match.group() if match else ""

    def extract_phone(self, text: str) -> str:

        match = re.search(
            r"(\+?\d[\d\s-]{8,}\d)",
            text,
        )

        return match.group() if match else ""