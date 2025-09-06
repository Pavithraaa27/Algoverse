from flask import Blueprint, request, jsonify
from utils.db import db, cursor  

messages_bp = Blueprint("messages", __name__)

@messages_bp.route("/", methods=["GET"])
def get_messages():
    cursor.execute("SELECT * FROM messages")
    messages = cursor.fetchall()
    return jsonify(messages)

@messages_bp.route("/", methods=["POST"])
def create_message():
    data = request.json
    content = data.get("content")

    cursor.execute("INSERT INTO messages (content) VALUES (%s)", (content,))
    db.commit()

    return jsonify({"message": "Message created successfully"})