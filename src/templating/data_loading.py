import os

from src.settings.dirs import DATA_DIR


def load_data(data_file_name):
    data_file_path = os.path.join(DATA_DIR, data_file_name)
    
    with open(data_file_path, 'r', encoding="utf-8") as f:
        content = f.read()
    
    return content
