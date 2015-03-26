from flask.ext.restful import Resource, Api
from models import db
from models.user import User

class UserListAPI(Resource):
    def get(self):
        users = [user.to_json() for user in User.query.all()]
        return Api.make_response(users, 200)

class UserAPI(Resource):
    def get(self, id):
        user = User.query.one()
        return user.to_json()
