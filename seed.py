from app import app, db
from models.workout import Workout
from models.exercise import Exercise
from models.workout_exercise import WorkoutExercise

with app.app_context():

    #  Clear old data (optional but recommended)
    WorkoutExercise.query.delete()
    Exercise.query.delete()
    Workout.query.delete()

    #  Create workouts
    w1 = Workout(name="Leg Day")
    w2 = Workout(name="Upper Body")

    #  Create exercises
    e1 = Exercise(name="Squats")
    e2 = Exercise(name="Bench Press")
    e3 = Exercise(name="Deadlift")

    db.session.add_all([w1, w2, e1, e2, e3])
    db.session.commit()

    #  Link exercises to workouts
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=e1.id, sets=3, reps=10)
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=e2.id, sets=4, reps=8)
    we3 = WorkoutExercise(workout_id=w1.id, exercise_id=e3.id, sets=5, reps=5)

    db.session.add_all([we1, we2, we3])
    db.session.commit()

    print(" Database seeded successfully!")