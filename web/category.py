#!/usr/bin/python3
from flask import Blueprint, Flask, redirect, render_template, request, url_for
from . import db
import uuid
from .models import Category, User
from flask_login import current_user

category = Blueprint('category', __name__)

@category.route('/create-category', methods=['POST'])
def create_category():
    category_name = request.form.get('categoryName')

    category = Category(id=uuid.uuid4(), category_name=category_name, user_id=current_user.id)
    db.session.add(category)
    db.session.commit()
    return redirect(url_for('views.profile'))

@category.route('/delete/<category_id>')
def delete_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category:
        if category.user_id == current_user.id:
            db.session.delete(category)
            db.session.commit()
    return redirect(url_for('views.profile'))

@category.route('/update/<category_id>', methods=['PUT'])
def update_category(category_id):
    category = Category.query.filter_by(id=category_id).first()
    if category:
        if category.user_id == current_user.id:
            category.category_name = 
            db.session.commit()
    return redirect(url_for('views.profile'))
