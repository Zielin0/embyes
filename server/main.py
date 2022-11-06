import re

from flask import Flask, request

# @TODO: Move hardcoded values to .env
host = "127.0.0.1"
port = 6969

hex_pattern = r"^#(?:[0-9a-fA-F]{3}){1,2}$"


def loadTemplate() -> str:
    template: str = ""
    with open("server/template.html", "r") as f:
        for line in f.readlines():
            template += str(line)
    return template


class OGMeta:
    # @TODO: Move it to another file
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


app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello, World!"


@app.route("/embed")
# @TODO: Rename embed to OG
def getEmbed() -> str:
    args = request.args
    if len(args) != 3:
        return "Not enough or too much args", 414

    color = args.get("color")
    title = args.get("title")
    description = args.get("description")

    if None in (color, title, description):
        return "Wrong args", 422

    meta = OGMeta(loadTemplate())
    try:
        return meta.format(f"#{color}", title, description)
    except ValueError as e:
        return f"{e}"


if __name__ == "__main__":
    app.run(host, port, True)
