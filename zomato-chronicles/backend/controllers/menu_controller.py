from models.menu import Dish
from db import get_db

def get_menu():
    db = get_db()
    menu_collection = db['menu']
    menu = list(menu_collection.find({}))
    return jsonify(menu)

def add_dish(dish_data):
    db = get_db()
    menu_collection = db['menu']
    dish = Dish(
        dish_id=dish_data['dish_id'],
        dish_name=dish_data['dish_name'],
        price=dish_data['price'],
        availability=dish_data['availability']
    )
    menu_collection.insert_one(dish.__dict__)
    response = {
        'message': 'Dish added successfully',
        'dish_id': dish.dish_id
    }
    return jsonify(response), 201

def remove_dish(dish_id):
    db = get_db()
    menu_collection = db['menu']
    menu_collection.delete_one({'dish_id': dish_id})
    response = {
        'message': f'Dish with dish_id {dish_id} removed successfully'
    }
    return jsonify(response)

def update_availability(dish_id, availability):
    db = get_db()
    menu_collection = db['menu']
    menu_collection.update_one(
        {'dish_id': dish_id},
        {'$set': {'availability': availability}}
    )
    response = {
        'message': f'Availability of dish with dish_id {dish_id} updated successfully'
    }
    return jsonify(response)
