from dataclasses import dataclass, field
from typing import List


@dataclass
class ResumeProfile:
    """
    Represents the structured information extracted
    from a resume.
    """

    name: str = ""
    email: str = ""
    phone: str = ""

    current_designation: str = ""

    total_experience: int = 0

    location: str = ""

    summary: str = ""

    skills: List[str] = field(default_factory=list)

    companies: List[str] = field(default_factory=list)

    domains: List[str] = field(default_factory=list)

    certifications: List[str] = field(default_factory=list)

    education: List[str] = field(default_factory=list)

    achievements: List[str] = field(default_factory=list)