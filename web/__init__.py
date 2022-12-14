from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils.functions import database_exists
from flask_login import LoginManager


db = SQLAlchemy()


def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo_dev:todo_dev_pwd@localhost/todo_db'
    app.config['SECRET_KEY'] = 'dev'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .category import category
    from .task import task

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(category, url_prefix='/')
    app.register_blueprint(task, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
