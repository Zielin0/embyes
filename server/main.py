from db.Database import Database
from flask import Flask, request
from modules.OGModule import OGModule
from psycopg2.errors import UniqueViolation
from template.Template import TemplateFile

app = Flask(__name__)


db: Database = None


@app.route("/")
def index() -> str:
    return "Hello, World!"


@app.route("/new", methods=["POST", "GET"])
# @TODO: implement rate limiting for this route
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

    image = args.get("image")
    small = args.get("small")

    if image == None and small == None:
        try:
            db.create_basic(url, color, title, description)
            return "Success"
        except UniqueViolation as e:
            return f"Failed to create embed. Row with url of '{url}' already exists"

    try:
        db.create_full(url, color, title, description, image, small)
        return "Success"
    except UniqueViolation as e:
        return f"Failed to create embed. Row with url of '{url}' already exists"


if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_cursor()
    app.run('0.0.0.0', 6969, True)
