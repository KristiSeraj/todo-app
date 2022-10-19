from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, default=0, autoincrement=True)
    user_name = db.Column(db.String(150))
    user_email = db.Column(db.String(150))
    user_password = db.Column(db.String(150))
