from flask import Flask
from flask_restful import Api

from .config import init_db, init_db_prod, init_db_tests
from .views import UsersAPI


def create_app(config=None):

    app = Flask(__name__)
    api = Api(app)

    if config == "test":
        init_db_tests()
    elif config == "prod":
        init_db_prod()
    else:
        init_db()

    api.add_resource(UsersAPI, "/user", "/user/<string:cpf>")

    @app.route('/')
    def home():
        return {"message": "this is an API"}

    return app
