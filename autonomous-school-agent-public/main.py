import os
import sys

# Add the project root to sys.path for proper imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.controller import HWBotController
from core.logger import logger

def run_mission():
    logger.info("Starting Autonomous Mission")
    bot = HWBotController()
    
    try:
        # STEP 1: Login
        if not bot.login():
            logger.error("Failed to login.")
            return

        # STEP 2: Discover Courses
        logger.info("Discovering courses...")
        courses = bot.crawl_courses()
        for course in courses:
            logger.info(f"Found Course: {course['title']}")

        # Implementation logic for specific assignments goes here
        # Example: bot.get_assignment("assignment_id")

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        bot.close()

if __name__ == "__main__":
    run_mission()
