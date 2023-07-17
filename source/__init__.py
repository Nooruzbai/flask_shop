import os
from datetime import timedelta
from os import environ

from flask import Flask
from .extensions import db, migrate, login_manager
from source.auth_app.user_models import User


def create_app():
    app = Flask(__name__,)

    secret_key = environ.get('SECRET_KEY')
    postgres_user = environ.get('POSTGRES_USER')
    postgres_password = environ.get('POSTGRES_PASSWORD')
    postgres_database = environ.get('POSTGRES_DB')
    upload_path = os.environ.get('UPLOAD_PATH')
    postgres_host = os.environ.get('POSTGRES_HOST')

    database_url = f'postgresql://{postgres_user}:{postgres_password}@localhost/{postgres_database}'
    app.config['SECRET_KEY'] = secret_key
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_PATH'] = upload_path

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    from source.auth_app.user_models import User

    @login_manager.user_loader
    def load_user(id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(id))

    with app.app_context():
        db.create_all()

    # blueprint for auth routes in our app
    from source.auth_app.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    # blueprint for non-auth parts of app
    from source.item_app.item import item as item_blueprint
    app.register_blueprint(item_blueprint)

    from source.cart_app.cart import cart as cart_blueprint
    app.register_blueprint(cart_blueprint)

    return app

