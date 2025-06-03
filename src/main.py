import pyperclip

from src.templating.template_population import get_populated_template
from src.settings.config import AUTO_COPY, AUTO_PRINT


def main(template_path):
    template_path_parts = template_path.split("/")
    assert len(template_path_parts) == 2, "Given template_path does not have 2 parts"

    template_category, template_name = template_path.split("/")
    populated_template = get_populated_template(template_category, template_name)

    if AUTO_COPY:
        pyperclip.copy(populated_template)
        print("Populated template copied to clipboard.")

    if AUTO_PRINT:
        print("Populated template:")
        print(populated_template)


if __name__ == "__main__":
    import argparse


    parser = argparse.ArgumentParser(description="")
    parser.add_argument(
        "--template_path",
        type=str,
        required=True,
        help="Path to the template file (required)"
    )
    
    args = parser.parse_args()
    main(args.template_path)
