import os
import time
from core.logger import logger

class ResourceCrawler:

    def __init__(self, schoology_client):
        self.schoology = schoology_client
        self.domain = schoology_client.domain

    def list_courses(self):
        logger.info("Listing enrolled courses...")
        self.schoology.page.goto(f"https://{self.domain}/courses")
        self.schoology.page.wait_for_load_state("networkidle")
        self.schoology.page.wait_for_selector(".courses-listing", timeout=15000)
        
        courses = []
        # Find all course list items
        course_items = self.schoology.page.query_selector_all(".course-item")
        for item in course_items:
            title_el = item.query_selector(".course-title")
            if not title_el: continue
            
            course_name = title_el.inner_text().strip()
            
            # Each course has one or more sections
            section_links = item.query_selector_all(".sections-list a")
            for link in section_links:
                section_name = link.inner_text().strip()
                href = link.get_attribute("href")
                courses.append({
                    "title": f"{course_name}: {section_name}",
                    "url": f"https://{self.domain}" + href,
                    "id": href.split("/")[-1]
                })
        
        logger.info(f"Discovered {len(courses)} courses/sections.")
        return courses

    def crawl_course_materials(self, course_id):
        url = f"https://{self.domain}/course/{course_id}/materials"
        logger.info(f"Crawling materials for course {course_id}...")
        self.schoology.page.goto(url)
        self.schoology.page.wait_for_load_state("networkidle")
        
        return self._crawl_folder_recursive(url, depth=0)

    def _crawl_folder_recursive(self, folder_url, depth=0):
        if depth > 3: return [] # Safety limit
        
        self.schoology.page.goto(folder_url)
        self.schoology.page.wait_for_load_state("networkidle")

        materials = []
        # Identify all items in the current view
        items = self.schoology.page.query_selector_all(".item-info")
        folder_urls = []

        for item in items:
            title_el = item.query_selector(".item-title a")
            if not title_el: continue
            
            title = title_el.inner_text().strip()
            href = title_el.get_attribute("href")
            item_url = f"https://{self.domain}" + href
            
            item_type = "unknown"
            if "/assignment/" in href:
                item_type = "assignment"
            elif "/folder/" in href:
                item_type = "folder"
                folder_urls.append(item_url)
            elif "/attachment/" in href:
                item_type = "file"

            materials.append({
                "title": title,
                "url": item_url,
                "type": item_type
            })

        # Recurse into folders
        for sub_url in folder_urls:
            sub_materials = self._crawl_folder_recursive(sub_url, depth + 1)
            materials.extend(sub_materials)
        
        return materials

    def find_overdue_assignments(self):
        logger.info("Checking for overdue assignments...")
        self.schoology.page.goto(f"https://{self.domain}/home")
        self.schoology.page.wait_for_load_state("networkidle")
        
        overdue = []
        overdue_items = self.schoology.page.query_selector_all(".overdue-list .upcoming-event")
        for item in overdue_items:
            link = item.query_selector("a")
            if link:
                overdue.append({
                    "title": link.inner_text().strip(),
                    "url": f"https://{self.domain}" + link.get_attribute("href"),
                    "details": item.inner_text().strip()
                })
        return overdue
