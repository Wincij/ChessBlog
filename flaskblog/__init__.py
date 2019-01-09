from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '66d4319be3000c0b2e975b48d113347b3815d92a5ba76b3bde6fe4e44757d38b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes
