from flask import Blueprint, render_template

urls = Blueprint('urls', __name__)


@urls.route("/url")
def index():
    return "URLs API"
