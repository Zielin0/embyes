if __name__ == "__main__":
    print("This is only include file. Do not run it.")
    exit(1)

import re

from template.Template import TemplateFile, loadTemplate

hex_pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"

# https://urlregex.com/
url_pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"


class OGModule:
    template: str = None

    def __init__(self, template: TemplateFile) -> None:
        self.template = loadTemplate(template)

    # Basic template check
    def check(self, color: str, title: str, description: str) -> bool:
        color_check: bool = True if re.search(hex_pattern, color) else False
        title_check: bool = True if len(title) <= 64 else False
        description_check: bool = True if len(description) <= 256 else False
        if color_check and title_check and description_check:
            return True

        return False

    # Full template check
    def check_full(self, color: str, title: str, description: str, image: str = "", small: str = "") -> bool:
        color_check: bool = True if re.search(hex_pattern, color) else False
        title_check: bool = True if len(title) <= 64 else False
        description_check: bool = True if len(description) <= 256 else False
        if len(image) > 0 and len(image) < 48:
            image_check: bool = True if re.search(
                url_pattern, image) else False
        image_check: bool = True if len(image) <= 48 else False
        small_check: bool = True if len(small) <= 32 else False
        if color_check and title_check and description_check and image_check and small_check:
            return True

        return False

    # Basic template format
    def format(self, color: str, title: str, description: str) -> str:
        if self.check(color, title, description):
            return self.template % (color, title, description)

        raise ValueError("Some of arguments didn't pass validation")

    # Full template format
    def format_full(self, color: str, title: str, description: str, image: str = "", small: str = "") -> str:
        if not image.startswith("http") or not image.startswith("https"):
            image = f"https://{image}"
        if self.check_full(color, title, description, image, small):
            return self.template % (color, title, description, image, small)

        raise ValueError("Some of arguments didn't pass validation")
