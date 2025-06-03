import os

from src.settings.dirs import TEMPLATES_DIR


def load_template(template_category, template_name):
    template_file_path = os.path.join(TEMPLATES_DIR, template_category, template_name)
    
    with open(template_file_path, 'r', encoding="utf-8") as f:
        content = f.read()
    
    return content
