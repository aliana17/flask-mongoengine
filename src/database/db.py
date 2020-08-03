from flask_mongoengine import MongoEngine

db = MongoEngine()

def initialized_db(ap):
    db.init_app(ap)