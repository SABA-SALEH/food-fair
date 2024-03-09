import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


if os.path.exists('env.py'):
    import env


app.config['SECRET_KEY'] = os.environ.get('saba')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from recipemanager import routes
