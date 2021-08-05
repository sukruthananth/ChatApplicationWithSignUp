import flask
from flask_sqlalchemy import SQLAlchemy
import config
from os import path
DB_NAME = "database.db"

app = flask.Flask(__name__, instance_relative_config=False)
app.config.from_object(config.Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

def create_database(app, db):
    if not path.exists('Website/' + DB_NAME):
        print("\n \nhas reached create table")
        db.create_all(app=app)

with app.app_context():
    db = SQLAlchemy(app)
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .database import User, Messages




