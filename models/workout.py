from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)

    #  TABLE VALIDATIONS
    name = db.Column(db.String(100), nullable=False, unique=True)

    # relationship
    workout_exercises = db.relationship(
        'WorkoutExercise',
        back_populates='workout',
        cascade='all, delete'
    )

    #  MODEL VALIDATION
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Workout name is required")
        if len(value) < 3:
            raise ValueError("Workout name must be at least 3 characters")
        return value