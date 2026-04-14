from marshmallow import Schema, fields, validates, ValidationError

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

    @validates("name")
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Exercise name too short")