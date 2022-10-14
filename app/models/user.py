#!/usr/bin/python3
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    user_id = db.Column(db.String(60), primary_key=True)
    user_name = db.Column(db.String(128), primary_key=True)
    user_email = db.Column(db.String(128), primary_key=True)
    user_password = db.Column(db.String(128), primary_key=True)

    def __repr__(self):
        return f'User{self.user_name}{self.email}'
