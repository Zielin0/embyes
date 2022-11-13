import os

from flask import Flask, request
from modules.OGModule import OGModule


def loadTemplate() -> str:
    template: str = ""
    with open(os.getcwd() + "/template.html", "r") as f:
        for line in f.readlines():
            template += str(line)
    return template


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

    meta = OGModule(loadTemplate())
    try:
        return meta.format(f"#{color}", title, description)
    except ValueError as e:
        return f"{e}"


if __name__ == "__main__":
    app.run('0.0.0.0', 6969, True)
