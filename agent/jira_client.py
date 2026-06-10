from jira import JIRA
from config.settings import Settings

class JiraClient:
    def __init__(self):
        s = Settings()
        self.jira = JIRA(
            server=s.jira_server,
            basic_auth=(s.jira_email, s.jira_token)
        )

    def get_story(self, story_key: str) -> dict:
        issue = self.jira.issue(story_key)
        fields = issue.fields
        return {
            "key": story_key,
            "summary": fields.summary,
            "description": fields.description or ""
        }