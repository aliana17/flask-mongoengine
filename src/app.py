import time
from flask import Flask, request, Response
from .database.db import initialized_db
from .database.models import Item

app = Flask(__name__)

"""items = [
    {
        "name": "Item1",
        "description": "A unique earing for fashion"
    },
    {
        "name": "Item1",
        "description": "A unique earing for fashion"
    }

]"""

app.config['MONGODB_SETTINGS'] = {
    'db': 'website-db',
    'host': 'mongodb://localhost/website-db'
}

db = initialized_db(app)

@app.route('/items')
def showItems():
    item = Item.objects().to_json()
    return  Response(item, mimetype='application/json', status=200)

@app.route('/additem', methods=['POST'])
def addItems():
    body = request.get_json(force=True)
    item = Item (name=body['name'], description=body['description'], price=body['price'])
    
    with open('item.jpg', 'rb') as fd:
        item.photo.put(fd, content_type = 'image/jpeg')
    item.save()

    id = item.id
    return {'id':str(id)}, 200

@app.route('/items/<int:index>', methods=['PUT'])
def updateItem(index):
    updateditem = request.get_json()
    Item.objects().get(id = index).update(**updateditem)
    return "",200

@app.route('/items/<int:index>', methods=['DELETE'])
def deleteItem(index):
    Item.objects().get(id = index).delete()
    return "",200

@app.route('/items/<int:index>', methods=['GET'])
def getsingleItem(index):
    particularItem = Item.objects().get(id=index).to_json()
    return Response(particularItem, mimetype='application/json', status=200)


