import os
from core.logger import logger
from browser.schoology_client import SchoologyClient
from browser.resource_crawler import ResourceCrawler
from core.file_processing.file_processor import FileProcessor
from core.organizer.organizer import Organizer
from core.prompt_builder.prompt_builder import PromptBuilder

class HWBotController:
    def __init__(self):
        env = self._parse_env()
        self.processor = FileProcessor()
        self.organizer = Organizer()
        self.builder = PromptBuilder()
        
        self.schoology = SchoologyClient(
            domain=env.get("SCHOOLOGY_DOMAIN"),
            username=env.get("SCHOOLOGY_EMAIL"),
            password=env.get("SCHOOLOGY_PASSWORD"),
            headless=env.get("HEADLESS", "True") == "True"
        )
        self.crawler = ResourceCrawler(self.schoology)

    def _parse_env(self):
        env = {}
        # New location for .env
        env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config", ".env")
        if os.path.exists(env_path):
            with open(env_path, "r") as f:
                for line in f:
                    if "=" in line and not line.startswith("#"):
                        key, value = line.split("=", 1)
                        value = value.strip().strip("'").strip('"')
                        value = value.replace("\\$", "$").replace("\\#", "#")
                        env[key] = value
        return env

    def login(self):
        return self.schoology.login()

    def crawl_courses(self):
        if not self.schoology.page:
            if not self.login(): return []
        return self.crawler.list_courses()

    def get_assignment(self, assignment_url):
        return self.schoology.get_assignment_data(assignment_url)

    def submit(self, url, file_path):
        return self.schoology.submit_assignment(url, file_path)

    def close(self):
        self.schoology.close()
