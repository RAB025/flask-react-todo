import json

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

TASKS_FILE = "tasks.json"

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})


# ---------------------------
# Helper functions
# ---------------------------

def load_tasks():
    """Load tasks from the JSON file."""
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    """Write tasks back to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def get_new_task_id(tasks):
    """Generate a new unique ID."""
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


# ---------------------------
# API Routes
# ---------------------------

@app.route("/")
def home():
    tasks = load_tasks()
    return jsonify(tasks)


@app.route("/tasks", methods=["POST"])
def add_task():
    tasks = load_tasks()
    data = request.get_json()

    new_task = {
        "id": get_new_task_id(tasks),
        "title": data.get("title"),
        "description": data.get("description", ""),
        "completed": False
    }

    tasks.append(new_task)
    save_tasks(tasks)

    return jsonify(new_task), 201


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)


@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)
    return {"error": "Task not found"}, 404


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    tasks = load_tasks()
    data = request.get_json()

    for task in tasks:
        if task["id"] == task_id:
            task["title"] = data.get("title", task["title"])
            task["description"] = data.get("description", task["description"])
            task["completed"] = data.get("completed", task["completed"])

            save_tasks(tasks)
            return jsonify(task)

    return {"error": "Task not found"}, 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            return {"message": "Task deleted successfully"}

    return {"error": "Task not found"}, 404


if __name__ == "__main__":
    app.run(debug=True)
