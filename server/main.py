from flask import Flask, request
from modules.OGModule import OGModule
from template.Template import TemplateFile, loadTemplate

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello, World!"


@app.route("/og")
def getOG() -> str:
    args = request.args
    if len(args) != 3:
        return "Not enough or too much args", 414

    color = args.get("color")
    title = args.get("title")
    description = args.get("description")

    if None in (color, title, description):
        return "Wrong args", 422

    meta = OGModule(loadTemplate(TemplateFile.TEMPLATE_BASIC))
    try:
        return meta.format(f"#{color}", title, description)
    except ValueError as e:
        return f"{e}"


if __name__ == "__main__":
    app.run('0.0.0.0', 6969, True)
