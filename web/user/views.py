#!/usr/bin/python3
from flask import Blueprint, flash, redirect, render_template, request, jsonify, abort
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField
from wtforms.validators import InputRequired
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from td_app.user.models import User, RegisterForm, LoginForm

user_bp = Blueprint('user_bp', __name__, template_folder='templates')

@user_bp.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegisterForm()

    if request.method == 'GET':
        return render_template('register.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User(user_name = form.name.data,
                    user_email = form.email.data,
                    user_password = generate_password_hash(form.password.data, method='sha256'))
            db.session.add(user)
            db.session.commit()
    return '<h1>New user has been created!</h1>'


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'GET':
        return render_template('login.html', form=form)

    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(user_email=form.email.data).first()
            if user:
                if check_password_hash(user.user_password, form.password.data):
                    login_user(user)
                    return redirect('/')


@user_bp.route('/logut')
@login_required
def logout():
    logout_user()
    return redirect('/')
