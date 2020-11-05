import os
from flask import Flask

# blueprint import
from blueprints.urls.views import urls
from blueprints.domains.views import domains
from blueprints.files.views import files
from blueprints.ip_address.views import ip_address


def create_app(app):
    # register blueprint
    app.register_blueprint(urls)
    app.register_blueprint(domains)
    app.register_blueprint(files)
    app.register_blueprint(ip_address)

    return app


if __name__ == "__main__":
    app = Flask(__name__)
    create_app(app).run(debug=True, port=9090)
