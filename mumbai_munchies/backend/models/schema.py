from marshmallow import Schema, fields

class SnackSchema(Schema):
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    availability = fields.Bool(required=True)

class SaleSchema(Schema):
    snack_id = fields.Str(required=True)
    quantity = fields.Int(required=True)
