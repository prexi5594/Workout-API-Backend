from flask import request
from app import app, db

from models.exercise import Exercise

@app.route("/exercises", methods=["GET"])
def get_exercises():
    return {"message": "get exercises"}

@app.route("/workouts/<int:id>/add-exercise", methods=["POST"])
def add_exercise(id):
    return {"message": "add exercise"}