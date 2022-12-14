import db.Environment as Env
from db.Database import Database
from flask import Flask, request
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from modules.OGModule import OGModule
from psycopg2.errors import StringDataRightTruncation, UniqueViolation
from template.Template import TemplateFile

app = Flask(__name__)
limiter = Limiter(app, key_func=get_remote_address)
CORS(app)

db: Database = None


@app.route("/")
def index() -> str:
    db.delete_all_expired()

    return "Hello, Embyes!", 200


@app.route("/<url>")
def getEmbed(url: str) -> str:
    try:
        if db.delete_expired(url):
            return "This URL has expired", 410
    except IndexError as e:
        return f"{e}", 400

    template: OGModule = None

    query = f"SELECT * FROM {Env.POSTGRES_DB} WHERE url = %s"
    db.cursor.execute(query, (url, ))

    row = db.cursor.fetchall()
    color = row[0][1]
    title = row[0][2]
    description = row[0][3]

    image = row[0][4]
    small = row[0][5]

    if None in (image, small):
        template = OGModule(TemplateFile.TEMPLATE_BASIC)
        try:
            return template.format(f"#{color}", title, description)
        except ValueError as e:
            return f"{e}"

    template = OGModule(TemplateFile.TEMPLATE_FULL)
    try:
        return template.format_full(f"#{color}", title, description, image, small)
    except ValueError as e:
        return f"{e}"


@app.route("/new", methods=["POST", "GET"])
@limiter.limit("30/minute")
def newOG() -> str:
    db.delete_all_expired()

    if request.method == "GET":
        return "This is `POST` only route.", 400

    args = request.args
    if len(args) < 4:
        return "Got less than 4 required args", 422

    if len(args) > 6:
        return "Request URL too long", 414

    url = args.get("url")
    color = args.get("color")
    title = args.get("title")
    description = args.get("description")

    if None in (url, color, title, description):
        return "Wrong args names", 422

    if "" in (url, color, title, description):
        return "Some of args are empty", 422

    image = args.get("image")
    small = args.get("small")

    if image == None and small == None:
        try:
            db.create_basic(url, color, title, description)
            return "Success", 201
        except UniqueViolation:
            return f"Failed to create embed. Row with url of '{url}' already exists", 409
        except StringDataRightTruncation:
            return "Some of parameters are too long", 409

    try:
        db.create_full(url, color, title, description, image, small)
        return "Success", 201
    except UniqueViolation:
        return f"Failed to create embed. Row with url of '{url}' already exists", 409
    except StringDataRightTruncation:
        return "Some of parameters are too long", 409


if __name__ == "__main__":
    db = Database()
    db.connect()
    db.create_cursor()
    db.delete_all_expired()
    app.run('0.0.0.0', 6969, True)
