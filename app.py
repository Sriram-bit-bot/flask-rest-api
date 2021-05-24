from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, Items
from resources.store import Store, StoreList

app =Flask(__name__)
app.secret_key ='4e5e487eb0d328f829233a75477b5ef0'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
api =Api(app)

jwt =JWT(app,authenticate,identity)
#jwt creates an endpoint '/auth' 

#Create the database instead of having a seperate file to do so
#We have returned item to just certify that the item has been received.
api.add_resource(Item,'/item/<string:name>')
api.add_resource(Items,'/items')
api.add_resource(UserRegister,'/register')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(StoreList, '/stores')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port =5000, debug =True)