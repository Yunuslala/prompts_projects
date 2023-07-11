from flask import Blueprint, request, jsonify
from app import mongo
from models.snack import Snack
from bson import ObjectId
snack_routes = Blueprint('snack_routes', __name__)
@snack_routes.route('/snacks', methods=['GET'])
def get_all_snacks():
    try:
        snacks = mongo.db.snacks.find()
        snack_list = []
        for snack in snacks:
            snack_data = Snack.from_dict(snack).to_dict()
            snack_data['_id'] = str(snack['_id'])  # Convert ObjectId to string
            snack_list.append(snack_data)
        return jsonify(snack_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@snack_routes.route('/snacks/<snack_id>', methods=['GET'])
def get_snack(snack_id):
    try:
        print (snack_id)
        inid = f"ObjectId('{snack_id}')"
        print(inid)
        snack = mongo.db.snacks.find_one({'_id':ObjectId(snack_id)})
        if snack:
            snack_data = Snack.from_dict(snack).to_dict()
            snack_data['_id'] = str(snack['_id'])  # Convert ObjectId to string
            return jsonify(snack_data), 200
        else:
            return jsonify({'message': 'Snack not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@snack_routes.route('/snacks', methods=['POST'])
def create_snack():
    try:
        data = request.get_json()
        snack = Snack(data['name'], data['price'], data['availability'])
        result = mongo.db.snacks.insert_one(snack.to_dict())
        if result.inserted_id:
            return jsonify({'message': 'Snack created successfully'}), 201
        else:
            return jsonify({'message': 'Failed to create snack'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@snack_routes.route('/snacks/<snack_id>', methods=['DELETE'])
def delete_snack(snack_id):
    try:
        result = mongo.db.snacks.delete_one({'_id': ObjectId(snack_id)})
        if result.deleted_count > 0:
            return jsonify({'message': 'Snack deleted successfully'}), 200
        else:
            return jsonify({'message': 'Snack not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
