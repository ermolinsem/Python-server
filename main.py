from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consumables1.db'

db = SQLAlchemy(app)

class Сonsumables(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    material = db.Column(db.String(50))
    quantity = db.Column(db.String(50))

    def __init__(self, name, material, quantity):
        self.name = name
        self.material = material
        self.quantity = quantity

with app.app_context():
    db.create_all()

@app.route('/add_consumables', methods=['POST'])
def add_consumables():
    name = request.form['name']
    material = request.form['material']
    quantity = request.form['quantity']
    consumables = Сonsumables(name, material, quantity)
    db.session.add(consumables)
    db.session.commit()
    return{"session": "Сonsumables added successfully"}

@app.route('/get_consumables/<int:id>')
def get_consumables(id):
    consumables = Сonsumables.query.get(id)
    if consumables:
        return jsonify({
            'id': consumables.id,
            'name': consumables.name,
            'material': consumables.material,
            'quantity': consumables.quantity
        })
    else:
        return {'error': 'Сonsumables not found'}

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug=True)