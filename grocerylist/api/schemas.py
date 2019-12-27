from marshmallow import Schema, fields

class UserCreds(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class GroceryItem(Schema):
    name = fields.Str(required=True)
    dollars = fields.Int(required=True)
    cents = fields.Int(required=True)
    checked = fields.Bool(required=True)
