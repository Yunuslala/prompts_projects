from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb+srv://saifjava2:saif@cluster0.7q0y1e1.mongodb.net/ZomatoDb?retryWrites=true&w=majority')
    return db
