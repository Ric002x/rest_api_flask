import mongoengine as db
from flask_restful import reqparse


class User(db.Document):
    cpf = db.StringField(required=True, unique=True)
    email = db.EmailField(required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    birth_date = db.DateTimeField(required=True)

    def repr(self):
        return {
            "cpf": self.cpf,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "birth_date": self.birth_date
        }

    @classmethod
    def find_by_cpf(cls, cpf):
        user = cls.objects(cpf=cpf)[0]
        return user.repr()

    @classmethod
    def all_users(cls):
        users = [user.repr() for user in cls.objects()]
        return users


parser = reqparse.RequestParser()

parser.add_argument('first_name', type=str, required=True)
parser.add_argument('last_name', type=str, required=True)
parser.add_argument('email', type=str, required=True)
parser.add_argument('cpf', type=str, required=True)
parser.add_argument('birth_date', type=str, required=True)
