from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.String(60), primary_key=True)
    user_name = db.Column(db.String(150))
    user_email = db.Column(db.String(150))
    user_password = db.Column(db.String(150))
"""
class Task(db.Model):
    id = db.Column(db.string(60), primary_key=True)
    task_name = db.Column(db.string(128), nullable=False)
    task_description = db.Column(db.string(1024))
    task_priority = db.Column(db.string(60), nullable=False)
    task_status = db.Column(db.string(60), nullable=False)
"""
