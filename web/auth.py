from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
import uuid
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_password = request.form.get('password')

        user = User.query.filter_by(user_email=user_email).first()
        if user:
            if check_password_hash(user.user_password, user_password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.profile'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_email = request.form.get('email')
        user_name = request.form.get('name')
        user_password = request.form.get('password')
        password_confirm = request.form.get('confirm_password')

        user = User.query.filter_by(user_email=user_email).first()

        if user:
            flash('Email already exists.', category='error')
        elif len(user_email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(user_name) < 2:
            flash('Name must be greater than 2 characters.', category='error')
        elif user_password != password_confirm:
            flash('Passwords don\'t match', category='error')
        elif len(password_confirm) < 7:
            flash('Password must be at least 7 character', category='error')
        else:
            user = User(user_name=user_name, user_email=user_email,
                        user_password=generate_password_hash(user_password,
                                                             method='sha256'))
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.profile'))

    return render_template('register.html', user=current_user)
