from flask import Flask, jsonify, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from models import User
from config import app_config

app = Flask(__name__)
app.config.from_object(app_config['development'])
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Import resources
from resources.signup import Signup
from resources.login import Login
from resources.logout import Logout
from resources.check_session import CheckSession

# Register resources
app.add_url_rule('/signup', view_func=Signup.as_view('signup'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
app.add_url_rule('/check_session', view_func=CheckSession.as_view('check_session'))

if __name__ == '__main__':
    app.run(debug=True)
