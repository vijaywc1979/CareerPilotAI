from pathlib import Path

from app.application import CareerPilotApplication
from agents.resume.resume_agent import ResumeAgent
from agents.resume.resume_extractor import ResumeExtractor

def main():

    app = CareerPilotApplication()
    app.start()

    agent = ResumeAgent()

    resume_text = agent.load_resume(
        Path("resume/Executive_Resume.docx")
    )

    extractor = ResumeExtractor()

    profile = extractor.extract(resume_text)

    print(profile)


if __name__ == "__main__":
    main()