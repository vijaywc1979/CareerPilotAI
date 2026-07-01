from infrastructure.database.database_manager import DatabaseManager
from domain.models.resume_profile import ResumeProfile


class ResumeRepository:

    def __init__(self):

        self.db = DatabaseManager()

    def save(self, profile: ResumeProfile):

        self.db.execute("""

        INSERT INTO resume_profile(

        name,

        email,

        phone,

        designation,

        experience,

        summary)

        VALUES(?,?,?,?,?,?)

        """,

        (

            profile.name,

            profile.email,

            profile.phone,

            profile.current_designation,

            profile.total_experience,

            profile.summary

        )

        )

    def get_latest(self):

        row = self.db.fetchone("""

        SELECT

        name,

        email,

        phone,

        designation,

        experience,

        summary

        FROM resume_profile

        ORDER BY id DESC

        LIMIT 1

        """)

        if row is None:

            return None

        profile = ResumeProfile()

        profile.name = row[0]
        profile.email = row[1]
        profile.phone = row[2]
        profile.current_designation = row[3]
        profile.total_experience = row[4]
        profile.summary = row[5]

        return profile