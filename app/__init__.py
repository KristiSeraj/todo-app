#!/usr/bin/python3
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo_dev:todo_dev_pwd@localhost/todo_db'
db = SQLAlchemy(app)

with app.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
