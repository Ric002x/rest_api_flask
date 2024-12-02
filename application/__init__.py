from flask import Flask
from flask_restful import Api

from .config import init_db
from .views import UserAPI

init_db()


def create_app(config=None):

    app = Flask(__name__)
    api = Api(app)

    api.add_resource(UserAPI, "/")

    return app
