import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    base_url: str = os.getenv("BASE_URL", "http://localhost:3000")
    api_base_url: str = os.getenv("API_BASE_URL", "http://localhost:8080")
    api_token: str = os.getenv("API_TOKEN", "")
    headless: bool = os.getenv("HEADLESS", "true").lower() == "true"
    jira_server: str = os.getenv("JIRA_SERVER", "")
    jira_email: str = os.getenv("JIRA_EMAIL", "")
    jira_token: str = os.getenv("JIRA_TOKEN", "")
    anthropic_api_key: str = os.getenv("ANTHROPIC_API_KEY", "")