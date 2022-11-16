import db.Database as DB
from flask import Flask, request
from modules.OGModule import OGModule
from template.Template import TemplateFile

app = Flask(__name__)


@app.route("/")
def index() -> str:
    return "Hello, World!"


@app.route("/new", methods=["POST", "GET"])
def newOG() -> str:
    # if request.method == "GET":
    #     return "This is `POST` only route.", 400

    template: OGModule = None

    args = request.args
    if len(args) < 4:
        return "Got less than 4 required args"

    url = args.get("url")
    color = args.get("color")
    title = args.get("title")
    description = args.get("description")

    if None in (url, color, title, description):
        return "Wrong args names", 422

    image = args.get("image") or ""
    small = args.get("small") or ""

    if image == "" and small == "":
        template = OGModule(TemplateFile.TEMPLATE_BASIC)
        # @TODO: Put basic OGModule into the database instead of showing it
        try:
            return template.format(f"#{color}", title, description)
        except ValueError as e:
            return f"{e}"

    # @TODO: Put full OGModule into the database instead of showing it
    template = OGModule(TemplateFile.TEMPLATE_FULL)
    try:
        return template.format_full(f"#{color}", title, description, image, small)
    except ValueError as e:
        return f"{e}"


if __name__ == "__main__":
    DB.connect()
    app.run('0.0.0.0', 6969, True)
