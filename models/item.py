from db import db

class ItemModel(db.Model):
    __tablename__ = "items"

    id =db.Column(db.Integer, primary_key =True)
    name =db.Column(db.String)
    price =db.Column(db.Float(precision =2))

    store_id =db.Column(db.Integer, db.ForeignKey('stores.id'))
    store =db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name =name
        self.price =price
        self.store_id =store_id

    def json(self):
        return {"name":self.name,"price":self.price}

    @classmethod
    def find_by_name(cls,name):
        #return ItemModel.query.filter_by(name =name) #SELECT * FROM items WHERE name=name
        return  cls.query.filter_by(name=name).first() #SELECT * FROM items WHERE name =name LIMIT 1
        #It returns the object itself

    def save_to_db(self):
        # connection =sqlite3.connect('data.db')
        # cursor =connection.cursor()
        # query ="INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, (self.name,self.price))

        # connection.commit()
        # connection.close()
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()