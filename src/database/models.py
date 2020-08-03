from .db import db

class Item(db.Document):
    index = db.IntField(required=True)
    name = db.StringField(required=True)
    description = db.StringField()
    price = db.IntField(required=True)
    photo = db.FileField(required=True)




