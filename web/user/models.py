#!/usr/bin/python3
from flask import Blueprint, flash, redirect, render_template, request, jsonify, abort
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from td_app.app import db
#user_bp.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://todo_dev:todo_dev_pwd@localhost/todo_db'
#user_bp.config['SECRET_KEY'] = 'dev'
#db = SQLAlchemy(user_bp)
#login_manager = LoginManager(user_bp)
#login_manager.init_app(user_bp)
#login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    user_id = db.Column(db.String(60), primary_key=True)
    user_name = db.Column(db.String(128), primary_key=True)
    user_email = db.Column(db.String(128), primary_key=True)
    user_password = db.Column(db.String(128), primary_key=True)

    def __repr__(self):
        return f'User{self.user_name}{self.email}'

#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    login = SubmitField('Login')

class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[InputRequired()])
    register = SubmitField('Register')
