from flask import Flask, Response, render_template, request, redirect, url_for
from datetime import date, timedelta
from models import Task
import db


app = Flask(__name__)


@app.route("/")  # This decorator is formed by our apps name ('app' in this case) and the 'route()' method.
def home() -> str:

    # Request to database (receives all elements, ordered by 'complete' state)
    assigments = db.session.query(Task).order_by(Task.complete.asc()).all()

    # Sets the actual day
    today = date.today()

    # Creates a new date-time object with the due days (7 days in that case)
    due_time = timedelta(days=7)

    # Sending tasks to front-end (including times)
    return render_template("index.html", all_assigments=assigments, today=today, due_time=due_time)


# This function allows to create a new task-type object with form data received,
# but needs to be setted with a route and a method. Both parts need to have the same name ("POST" in this case)
@app.route("/create-task", methods=["POST"])  # 'POST' is an HTTP method
def create_task() -> Response:

    day = date.today()  # Stores the day
    data = request.form  # Stores form in dictionary format

    # Creates the new task
    task = Task(
        content=data["task_content"],
        complete=False,
        category=data["category"],
        created=day
    )

    # Adds the task to database
    db.session.add(task)

    # Saves any change
    db.session.commit()

    # Redirect to 'home'
    return redirect(url_for("home"))


# This function allows to request for an unique element by 'id'. The name on 'app.route' and 'function argument'
# must be de same.
@app.route("/task-complete/<task_id>")
def task_complete(task_id: int) -> Response:

    # Request to database. Casts 'task_id' to integer just in case.
    task = db.session.query(Task).filter(Task.id == int(task_id)).first()

    # Changes the element status
    task.complete = not task.complete

    # Saves any change
    db.session.commit()

    # Redirect to 'home'
    return redirect(url_for("home"))


@app.route("/delete-task/<task_id>")
def delete_task(task_id: int) -> Response:

    # Request to database. Casts 'task_id' to integer just in case.
    db.session.query(Task).filter(Task.id == int(task_id)).delete()

    # Saves any change
    db.session.commit()

    # Redirect to 'home'
    return redirect(url_for("home"))


@app.route("/update-task/<task_id>")
def update_task(task_id: int) -> str:

    # New request using task ID
    data = db.session.query(Task).filter(Task.id == int(task_id)).first()

    # Sets the actual day
    today = date.today()

    # Loads the new web page with necessary data
    return render_template("update_task.html", task=data, today=today)


@app.route("/updated/<task_id>", methods=["POST"])
def updated(task_id: int):

    # Get the data from front-end
    data = request.form

    # New request using the same ID
    task = db.session.query(Task).filter(Task.id == int(task_id)).first()

    # Sets the actual day
    today = date.today()

    # Modifies the database
    if data["task_content"] != "":
        task.content = data["task_content"]
        task.category = data["category"]
        task.created = today

    else:
        task.category = data["category"]
        task.created = today    # Save all changes
    db.session.commit()

    # Go back to home
    return redirect(url_for("home"))


def main() -> None:

    # Creates the database
    db.Base.metadata.create_all(bind=db.engine)

    # Runs the server
    app.run(debug=True)


if __name__ == '__main__':
    main()
