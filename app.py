from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# Configure MongoDB connection
app.config['MONGODB_SETTINGS'] = {
    'db': 'store',
    'host': 'mongodb+srv://saifjava2:saif@cluster0.iqu5lya.mongodb.net/?retryWrites=true&w=majority',
    'connect': False  # Set to False to defer connection until needed
}

db = MongoEngine(app)


# Define schema models
class User(db.Document):
    name = db.StringField(required=True)
    age = db.IntField()


# Routes
@app.route('/api/data', methods=['GET'])
def get_data():
    users = User.objects()
    result = []
    for user in users:
        result.append({
            'id': str(user.id),
            'name': user.name,
            'age': user.age
        })
    return jsonify(result)


@app.route('/api/data', methods=['POST'])
def create_data():
    data = request.get_json()
    name = data['name']
    age = data['age']
    new_user = User(name=name, age=age)
    new_user.save()
    return jsonify({'message': 'Data created successfully'})


if __name__ == '__main__':
    app.run()
