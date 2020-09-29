from flask import render_template, request, redirect

from app import flask_app, db
from app.models import User, Task

# tasks INDEX
@flask_app.route('/tasks')
def index():
    user = User.query.get(1)
    tasks = user.tasks
    return render_template("index.html", title="todo_list", user=user, tasks=tasks)

@flask_app.route('/tasks', methods=['POST'])
def create_task():
    title = request.form["title"]
    description = request.form["description"]
    current_user = User.query.get(1)
    new_task = Task(title=title, description=description, user=current_user)

    db.session.add(new_task)
    db.session.commit()

    return redirect('/tasks')

@flask_app.route('/tasks/<int:task_id>', methods=['POST'])
def update_task(task_id):
    task_to_update = Task.query.get(task_id)
    task_to_update.done = True

    db.session.commit()

    return redirect('/tasks')

#  USERS INDEX
@flask_app.route('/users')
def users():
    return "list of all users here"