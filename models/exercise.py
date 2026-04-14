from app import db
from sqlalchemy.orm import validates




class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)

    #  TABLE VALIDATIONS
    name = db.Column(db.String(100), nullable=False, unique=True)

    # relationship
    workout_exercises = db.relationship(
        'WorkoutExercise',
        back_populates='exercise',
        cascade='all, delete'
    )

    #  MODEL VALIDATION
    @validates('name')
    def validate_name(self, key, value):
        if not value:
            raise ValueError("Exercise name is required")
        if len(value) < 2:
            raise ValueError("Exercise name too short")
        return value