import re

hex_pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"


class OGModule:
    template = None

    def __init__(self, template: str) -> None:
        self.template = template

    def check(self, color: str, title: str, description: str) -> bool:
        color_check: bool = True if re.search(hex_pattern, color) else False
        title_check: bool = True if len(title) <= 64 else False
        description_check: bool = True if len(description) <= 1024 else False
        if color_check and title_check and description_check:
            return True
        else:
            return False

    # @TODO: Add images and possibly links
    # @TODO: would need database tho cause links will be too long
    # @TODO: If adding a database consider adding custom links and their expiry
    def format(self, color: str, title: str, description: str) -> str:
        if self.check(color, title, description):
            return self.template % (color, title, description)
        else:
            raise ValueError("Some of arguments didn't pass validation")


if __name__ == "__main__":
    print("This is only include file. Do not run it.")
    exit(1)