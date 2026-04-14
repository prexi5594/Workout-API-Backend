from marshmallow import Schema, fields, validates, ValidationError

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

    @validates("name")
    def validate_name(self, value):
        if len(value) < 3:
            raise ValidationError("Workout name must be at least 3 characters")