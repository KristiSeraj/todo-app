from . import db
from flask_login import UserMixin

task_category = db.Table('task_category',
                        db.Column('task_id', db.String(60), db.ForeignKey('task.id')),
                        db.Column('category_id', db.String(60), db.ForeignKey('category.id'))
                )

class User(db.Model, UserMixin):
    id = db.Column(db.String(60), primary_key=True)
    user_name = db.Column(db.String(150))
    user_email = db.Column(db.String(150))
    user_password = db.Column(db.String(150))
    user_category = db.relationship('Category', backref='user')
    user_task = db.relationship('Task', backref='user')

class Task(db.Model):
    id = db.Column(db.String(60), primary_key=True)
    task_name = db.Column(db.String(128), nullable=False)
    task_description = db.Column(db.String(1024))
    task_priority = db.Column(db.String(60), nullable=False)
    #task_status = db.Column(db.String(128), nullable=False)
    categories = db.relationship('Category', secondary=task_category, backref='tasks')
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'))

class Category(db.Model):
    id = db.Column(db.String(60), primary_key=True)
    category_name = db.Column(db.String(128))
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'))
