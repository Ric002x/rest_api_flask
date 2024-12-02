from flask import jsonify
from flask_restful import Resource

from .models import User, parser


class UserAPI(Resource):
    def post(self):
        data = parser.parse_args()
        user = User(**data)
        user.save()
        return data

    def get(self):
        users = User.objects()  # type: ignore
        return jsonify([user.to_json() for user in users])
