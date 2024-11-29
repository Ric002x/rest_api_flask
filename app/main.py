import mongoengine as db
from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

db.connect(
    host="mongodb://admin:admin-password@mongodb:27017/userdb?authSource=admin"
)


class User(db.Document):
    cpf = db.StringField(required=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)

    def __repr__(self):
        return {
            "cpf": self.cpf,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birth_date": self.birth_date,
        }


class HelloWorld(Resource):
    def get(self):
        users = [user.to_mongo().to_dict()
                 for user in User.objects()]  # type: ignore
        return jsonify(users)


api.add_resource(HelloWorld, "/")
