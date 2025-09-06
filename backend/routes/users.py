from flask import Blueprint, request, jsonify
from utils.db import db, cursor

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    cursor.execute("SELECT id, name, email, phone, avatar_url, created_at FROM users WHERE id=%s", (user_id,))
    user = cursor.fetchone()
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404

@users_bp.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    data = request.get_json()
    cursor.execute(
        "UPDATE users SET name=%s, phone=%s, avatar_url=%s WHERE id=%s",
        (data.get('name'), data.get('phone'), data.get('avatar_url'), user_id)
    )
    db.commit()
    return jsonify({'message': 'Profile updated successfully'})