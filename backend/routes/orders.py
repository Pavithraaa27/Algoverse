from flask import Blueprint, request, jsonify
from utils.db import db, cursor

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/orders', methods=['POST'])
def place_order():
    data = request.get_json()
    user_id = data.get('user_id')

    cursor.execute("SELECT * FROM cart_items ci JOIN carts c ON ci.cart_id=c.id WHERE c.user_id=%s", (user_id,))
    items = cursor.fetchall()
    if not items:
        return jsonify({'error': 'Cart is empty'}), 400

    total = sum(item['qty'] * item['price'] for item in items)

    cursor.execute("INSERT INTO orders (buyer_id, total) VALUES (%s,%s)", (user_id, total))
    db.commit()
    order_id = cursor.lastrowid

    for item in items:
        cursor.execute(
            "INSERT INTO order_items (order_id, product_id, price_at_purchase, qty) VALUES (%s,%s,%s,%s)",
            (order_id, item['product_id'], item['price'], item['qty'])
        )
    cursor.execute("DELETE FROM cart_items WHERE cart_id=%s", (items[0]['cart_id'],))
    db.commit()

    return jsonify({'message': 'Order placed successfully', 'order_id': order_id})