
from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os
load_dotenv('.env')
app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('mongourl')
mongo = PyMongo(app)

if __name__ == '__main__':
    from routes.snack_routes import snack_routes
    from routes.sale_routes import sale_routes
    
    app.register_blueprint(snack_routes)
    app.register_blueprint(sale_routes)
    
    app.run(debug=True, port=8000)
