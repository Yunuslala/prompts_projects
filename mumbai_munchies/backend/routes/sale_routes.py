from flask import Blueprint, jsonify, request
from models.schema import SaleSchema
from app import mongo
from bson import ObjectId

sale_routes = Blueprint('sale_routes', __name__)
sale_schema = SaleSchema()

@sale_routes.route('/sales', methods=['POST'])
def record_sale():
    data = request.json
    errors = sale_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    sale = {
        'snack_id': data['snack_id'],
        'quantity': data['quantity']
    }
    mongo.db.sales.insert_one(sale)
    snack_id = data['snack_id'] 
    result = mongo.db.snacks.update_one({'_id': ObjectId(snack_id)}, {'$set': {'availability': False}})
    print(result)
    return jsonify({'message': 'Sale recorded successfully'})
@sale_routes.route('/sales', methods=['GET'])
def get_all_sales():
    try:
        sales = mongo.db.sales.find()
        sale_list = []
        for sale in sales:
            sale_data = {
                'snack_id': sale['snack_id'],
                'quantity': sale['quantity'],
                '_id': str(sale['_id'])  # Convert ObjectId to string
            }
            sale_list.append(sale_data)
        return jsonify(sale_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500