from flask.ext.restful import Resource, marshal_with
from models import db
from models.user import User

class UserListAPI(Resource):
    @marshal_with(User._fields())
    def get(self):
        users = User.query.all()
        return users

class UserAPI(Resource):
    @marshal_with(User._fields())
    def get(self, id):
        user = User.query.one()
        return user
