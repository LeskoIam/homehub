from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from homehub.common.common import format_datetime
from homehub_web.config import Config


app = Flask(__name__)
app.config.from_object(Config)

login = LoginManager(app)

db = SQLAlchemy(app)

# app.jinja_env.filters['format_datetime'] = format_datetime

from homehub_web import views
