#!/usr/bin/env python3
''' entry point '''
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
  ''' Product Model '''
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(225), unique=True)
  description = db.Column(db.String(450))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer)

  def __init__(self, name, description, price, qty):
    self.name = name
    self.description = description
    self.price = price
    self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

# Init Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route('/product', methods=['POST'], strict_slashes=False)
def add_product():
  ''' create a new product '''
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']
  new_product = Product(name, description, price, qty)

  with app.app_context():
    db.session.add(new_product)
    db.session.commit()

  return product_schema.jsonify(new_product)


# Get all products
@app.route('/products', methods=['GET'], strict_slashes=False)
def get_products():
  ''' get products '''
  all_products = Product.query.all()
  result = products_schema.dump(all_products)
  return jsonify(result), 200


# get single product
@app.route('/products/<product_id>', methods=['GET'], strict_slashes=False)
def get_product(product_id):
  ''' get product by ID '''
  product = Product.query.get(product_id)
  return product_schema.jsonify(product)


# update product
@app.route('/product/<product_id>', methods=['PUT'], strict_slashes=False)
def update_product(product_id):
  ''' update product '''
  product = Product.query.get(product_id)

  if product is None:
    return jsonify({"error": "Product not found"}), 404

  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)


# delete product
@app.route('/products/<product_id>', methods=['DELETE'], strict_slashes=False)
def del_product(product_id):
  ''' get product by ID '''
  product = Product.query.get(product_id)

  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)


# Run server
if __name__ == "__main__":
  app.run(debug=True, port=5000)
