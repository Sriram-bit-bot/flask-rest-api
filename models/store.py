from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id =db.Column(db.Integer, primary_key =True)
    name =db.Column(db.String)
    price =db.Column(db.Float(precision =2))

    items =db.relationship('ItemModel', lazy ='dynamic')
 
    def __init__(self, name):
        self.name =name

    def json(self):
        return {"name":self.name,"items":[item.json() for item in self.items.all()]}

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