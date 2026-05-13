import os
import shutil
from core.logger import logger

class Organizer:
    def __init__(self, base_dir="hwbot_output"):
        self.base_dir = base_dir

    def create_structure(self, class_name, assignment_name):
        safe_class = "".join([c if c.isalnum() else "_" for c in class_name])
        safe_assignment = "".join([c if c.isalnum() else "_" for c in assignment_name])
        
        root = os.path.join(self.base_dir, safe_class, safe_assignment)
        raw = os.path.join(root, "raw_materials")
        extracted = os.path.join(root, "extracted_text")

        os.makedirs(raw, exist_ok=True)
        os.makedirs(extracted, exist_ok=True)

        return {
            "root": root,
            "raw": raw,
            "extracted": extracted,
            "prompt_file": os.path.join(root, "prompt.txt")
        }
