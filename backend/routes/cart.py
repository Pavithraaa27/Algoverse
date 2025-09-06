from flask import Blueprint, request, jsonify
from utils.db import db, cursor

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    cursor.execute("SELECT * FROM cart_items ci JOIN carts c ON ci.cart_id=c.id WHERE c.user_id=%s", (user_id,))
    return jsonify(cursor.fetchall())

@cart_bp.route('/cart/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    qty = data.get('qty', 1)

    cursor.execute("SELECT id FROM carts WHERE user_id=%s", (user_id,))
    cart = cursor.fetchone()
    if not cart:
        cursor.execute("INSERT INTO carts (user_id) VALUES (%s)", (user_id,))
        db.commit()
        cursor.execute("SELECT id FROM carts WHERE user_id=%s", (user_id,))
        cart = cursor.fetchone()

    cart_id = cart['id']

    cursor.execute(
        "INSERT INTO cart_items (cart_id, product_id, qty) VALUES (%s,%s,%s) ON DUPLICATE KEY UPDATE qty=qty+%s",
        (cart_id, product_id, qty, qty)
    )
    db.commit()
    return jsonify({'message': 'Added to cart'})