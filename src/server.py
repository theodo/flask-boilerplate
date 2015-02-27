import config
from flask import Flask
from flask.ext.cors import CORS
from models import db

server = Flask(__name__)
server.debug = config.DEBUG
server.config['SQLALCHEMY_DATABASE_URI'] = config.DB_URI
db.init_app(server)

CORS(server, resources={r"/*": {"origins": "*"}}, headers=['Content-Type', 'X-Requested-With', 'Authorization'])

from routes.user import user_blueprint
server.register_blueprint(user_blueprint)

if __name__ == '__main__':
    server.run(host=config.HOST, port=config.PORT)
