from flask import jsonify
from flask_restful import Resource
from mongoengine import NotUniqueError

from .models import User, parser


class UsersAPI(Resource):
    def post(self):
        data = parser.parse_args()
        user = User(**data)
        try:
            response = user.save()
            return {"message": f"User {response.id} successfully created!"}
        except NotUniqueError:
            return {"message": f"User with cpf {user.cpf} already exist"}, 400

    def get(self, cpf=None):
        if cpf:
            try:
                user = User.find_by_cpf(cpf)
                return jsonify(user)
            except IndexError:
                return {"message": "User not Found"}, 404
        else:
            return jsonify(User.all_users())
