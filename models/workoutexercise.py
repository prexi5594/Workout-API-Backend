from app import db
from sqlalchemy.orm import validates



class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)

    # foreign keys
    workout_id = db.Column(
        db.Integer,
        db.ForeignKey('workouts.id'),
        nullable=False
    )

    exercise_id = db.Column(
        db.Integer,
        db.ForeignKey('exercises.id'),
        nullable=False
    )

    # extra fields
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer)
    duration = db.Column(db.Integer)

    # relationships
    workout = db.relationship('Workout', back_populates='workout_exercises')
    exercise = db.relationship('Exercise', back_populates='workout_exercises')

    # ✅ TABLE CONSTRAINT
    __table_args__ = (
        db.CheckConstraint('sets > 0', name='check_sets_positive'),
    )

    # ✅ MODEL VALIDATIONS
    @validates('sets')
    def validate_sets(self, key, value):
        if value <= 0:
            raise ValueError("Sets must be greater than 0")
        return value

    @validates('reps')
    def validate_reps(self, key, value):
        if value is not None and value < 0:
            raise ValueError("Reps cannot be negative")
        return value

    @validates('duration')
    def validate_duration(self, key, value):
        if value is not None and value < 0:
            raise ValueError("Duration cannot be negative")
        return value