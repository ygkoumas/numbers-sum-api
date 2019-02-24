from flask import Flask
from total import total

def create_app():
    app = Flask(__name__)
    app.register_blueprint(total, url_prefix="/total")
    return app
