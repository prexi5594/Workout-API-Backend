from marshmallow import Schema, fields, validates, ValidationError

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)

    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)

    sets = fields.Int(required=True)
    reps = fields.Int()
    duration = fields.Int()

    @validates("sets")
    def validate_sets(self, value):
        if value <= 0:
            raise ValidationError("Sets must be greater than 0")