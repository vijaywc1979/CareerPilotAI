from pathlib import Path

from app.application import CareerPilotApplication
from agents.resume.resume_agent import ResumeAgent


def main():

    app = CareerPilotApplication()
    app.start()

    agent = ResumeAgent()

    resume_text = agent.load_resume(
        Path("resume/Executive_Resume.docx")
    )

    print("\n")
    print("=" * 80)
    print("RESUME PREVIEW")
    print("=" * 80)

    print(resume_text[:3000])


if __name__ == "__main__":
    main()