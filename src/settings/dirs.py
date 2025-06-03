import os


SETTINGS_DIR = os.path.dirname(__file__)
SRC_DIR = os.path.dirname(SETTINGS_DIR)
REPO_DIR = os.path.dirname(SRC_DIR)

TEMPLATES_DIR = os.path.join(REPO_DIR, "templates")
PROMPT_TEMPLATES_DIR = os.path.join(TEMPLATES_DIR, "prompts")

DATA_DIR = os.path.join(REPO_DIR, "data")

assert os.path.exists(PROMPT_TEMPLATES_DIR) and os.path.isdir(PROMPT_TEMPLATES_DIR), \
    f"PROMPT_TEMPLATES_DIR does not exist at {PROMPT_TEMPLATES_DIR}"
assert os.path.exists(DATA_DIR) and os.path.isdir(DATA_DIR), \
    f"DATA_DIR does not exist at {DATA_DIR}"
