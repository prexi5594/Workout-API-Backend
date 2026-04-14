from flask import request
from app import app, db
from models.workout import Workout
from models.workout_exercise import WorkoutExercise
from schemas.workout_schema import WorkoutSchema

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

from flask import request
from app import app

@app.route("/workouts", methods=["GET"])
def get_workouts():
    return {"message": "get workouts"}

@app.route("/workouts", methods=["POST"])
def create_workout():
    return {"message": "create workout"}

@app.route("/workouts/<int:id>", methods=["DELETE"])
def delete_workout(id):
    return {"message": "delete workout"}

