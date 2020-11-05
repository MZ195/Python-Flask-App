from flask import Blueprint

domains = Blueprint('domains', __name__)


@domains.route("/domain")
def list_of_clothes():
    return "Domains API"
