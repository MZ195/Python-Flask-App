from flask import Blueprint


files = Blueprint('files', __name__)


@files.route("/file")
def contact_me():
    return "files API"
