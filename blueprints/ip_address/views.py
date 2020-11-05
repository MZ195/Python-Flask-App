from flask import Blueprint
import requests

ip_address = Blueprint('ip_address', __name__)


@ip_address.route("/ip_address")
def ip_address_home():
    return "ip_address API"
