import mongoengine as db
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

db.connect(
    host="mongodb://admin:admin-password@mongodb:27017/user_db"
)


class User(db.Document):
    cpf = db.StringField(required=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


class HelloWorld(Resource):
    def get(self):
        return {"Hello": "World"}


api.add_resource(HelloWorld, "/")
