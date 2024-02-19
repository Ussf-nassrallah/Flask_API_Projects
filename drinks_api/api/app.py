from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

# Drink Model
class Drink(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(220))

  def __repr__(self):
    return f"{self.name} - {self.description}"


@app.route('/')
def index():
  return 'Hello!'


# get all drinks data
@app.route('/drinks', methods=['GET'])
def get_drinks():
  drinks = Drink.query.all()
  output = []

  for drink in drinks:
    drink_data = {
      'id': drink.id,
      'name': drink.name,
      'description': drink.description
    }
    output.append(drink_data)

  return {'drinks': output}


# get a single drink data by id
@app.route('/drinks/<id>', methods=['GET'])
def get_drink(id):
  drink = Drink.query.get_or_404(id)
  return {'name': drink.name, 'description': drink.description}


# create a new Drink
@app.route('/drinks', methods=['POST'])
def add_drink():
  drink = Drink(name=request.json['name'], description=request.json['description'])
  db.session.add(drink)
  db.session.commit()
  return {'id': drink.id}


# DELETE drink
@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
  drink = Drink.query.get(id)

  if drink is None:
    return {"error": "not found!"}

  db.session.delete(drink)
  db.session.commit()

  return {"message": "drink obj deleted successfully"}


# update drink
@app.route('/drinks/<id>', methods=['PUT'])
def update_drink(id):
  drink = Drink.query.get(id)

  if drink is None:
    return {"error": "not found!"}

  drink.name = request.json['name']
  drink.description = request.json['description']
  db.session.commit()

  return {"message": f"drink [{drink.id}]: updated successfully"}


if __name__ == "__main__":
  app.run(debug=True)