#!/usr/bin/python3
from flask import Flask
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo_dev:todo_dev_pwd@localhost/todo_db'
app.config['SECRET_KEY'] = 'dev'
db = SQLAlchemy(app)

with app.app_context():
    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    from .user.views import user_bp
    app.register_blueprint(user_bp)

    from .user.models import User
    db.create_all()
    db.session.commit()

login_manager = LoginManager()
login_manager.init_app(user_bp)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
