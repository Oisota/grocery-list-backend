from marshmallow import Schema, fields

class UserCreds(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
