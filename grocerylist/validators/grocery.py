"""Grocery Validators"""

from marshmallow import Schema, fields

class GroceryItemValidator(Schema):
    name = fields.Str(required=True)
    dollars = fields.Int(required=True)
    cents = fields.Int(required=True)
    checked = fields.Bool(required=True)
