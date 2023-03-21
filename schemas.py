from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True)
    added_date = fields.DateTime(dump_only=True)


class UserUpdateSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    phone_number = fields.Str()


class UserDeleteSchema(Schema):
    id = fields.Int(required=True)
