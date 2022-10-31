#!/usr/bin/python3
from flask import Blueprint, Flask, redirect, render_template, request, url_for
from . import db
import uuid
from .models import Category, User, Task
from flask_login import current_user

task = Blueprint('task', __name__)

@task.route('/create-task', methods=['POST'])
def create_task():
    task_name = request.form.get('taskName')
    task_description = request.form.get('taskDescription')
    task_priority = request.form.get('priorityName')
    task_category = request.form.getlist('taskCategory')
    task = Task(id=uuid.uuid4(), task_name=task_name, task_description=task_description, task_priority=task_priority, categories=[task_category], user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    return redirect(url_for('views.profile'))

@task.route('/delete-task/<task_id>')
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id).first()
    if task:
        if task.user_id == current_user.id:
            db.session.delete(task)
            db.session.commit()
    return redirect(url_for('views.profile'))
