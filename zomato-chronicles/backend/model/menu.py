from pymongo import MongoClient
from bson import ObjectId
from bson.json_util import dumps
from jsonschema import validate, ValidationError

# Define the schema for the "menu" collection
menu_schema = {
    'type': 'object',
    'properties': {
        '_id': {'type': 'string', 'pattern': '^[0-9a-fA-F]{24}$'},
        'dish_id': {'type': 'integer'},
        'dish_name': {'type': 'string'},
        'price': {'type': 'number'},
        'availability': {'type': 'boolean'}
    },
    'required': ['dish_id', 'dish_name', 'price', 'availability'],
    'additionalProperties': False
}

# Example data for validation
dish = {
    'dish_id': 1,
    'dish_name': 'Pizza',
    'price': 12.99,
    'availability': True
}

# Validate the dish data against the schema
try:
    validate(dish, menu_schema)
    print("Data is valid according to the schema.")
except ValidationError as e:
    print("Data validation failed.")
    print(e)
