from flask import Blueprint, request, jsonify
from utils.db import db, cursor

products_bp = Blueprint('products', __name__)

@products_bp.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    cursor.execute(
        "INSERT INTO products (user_id, category_id, title, description, price, condition, location, quantity) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            data.get('user_id'), data.get('category_id'), data.get('title'),
            data.get('description'), data.get('price'), data.get('condition'),
            data.get('location'), data.get('quantity')
        )
    )
    db.commit()
    return jsonify({'message': 'Product added successfully'})

@products_bp.route('/products', methods=['GET'])
def list_products():
    cursor.execute("SELECT * FROM products WHERE is_active=1")
    return jsonify(cursor.fetchall())

@products_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    cursor.execute("SELECT * FROM products WHERE id=%s", (product_id,))
    product = cursor.fetchone()
    return jsonify(product if product else {'error': 'Product not found'})

@products_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    cursor.execute(
        "UPDATE products SET title=%s, description=%s, price=%s, condition=%s, location=%s, quantity=%s WHERE id=%s",
        (
            data.get('title'), data.get('description'), data.get('price'),
            data.get('condition'), data.get('location'), data.get('quantity'), product_id
        )
    )
    db.commit()
    return jsonify({'message': 'Product updated successfully'})

@products_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    cursor.execute("DELETE FROM products WHERE id=%s", (product_id,))
    db.commit()
    return jsonify({'message': 'Product deleted successfully'})