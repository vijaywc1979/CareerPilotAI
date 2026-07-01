from pathlib import Path

from pathlib import Path

from app.application import CareerPilotApplication
from agents.resume.resume_agent import ResumeAgent
from agents.resume.resume_extractor import ResumeExtractor
from domain.repositories.resume_repository import ResumeRepository

def main():

    app = CareerPilotApplication()
    app.start()

    agent = ResumeAgent()

    resume_text = agent.load_resume(
        Path("users/vijayan/resume/Executive_Resume.docx")
    )

    extractor = ResumeExtractor()

    profile = extractor.extract(resume_text)
    repository = ResumeRepository()

    print("\nSaving Resume Profile...")

    repository.save(profile)

    print("Profile Saved.")

    print("\nLoading Resume Profile...")

    saved_profile = repository.get_latest()

    print(saved_profile)

if __name__ == "__main__":
    main()