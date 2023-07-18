from flask import Blueprint, render_template
from models.task_list import tasks_from_python

tasks_blueprint=Blueprint("tasks",__name__)

@tasks_blueprint.route("/tasks")
def index():
    return render_template("index.html",title="my task list",tasks_for_jinja=tasks_from_python)