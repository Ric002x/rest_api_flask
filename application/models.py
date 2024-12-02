import mongoengine as db
from flask_restful import reqparse


class User(db.Document):
    cpf = db.StringField(required=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)


parser = reqparse.RequestParser()

parser.add_argument('first_name', type=str, required=True)
parser.add_argument('last_name', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('cpf', type=str, required=True)
parser.add_argument('birth_date', type=str, required=True)
