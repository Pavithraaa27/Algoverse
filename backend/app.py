from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.users import users_bp
from routes.products import products_bp
from routes.cart import cart_bp
from routes.orders import orders_bp
from routes.messages import messages_bp

app = Flask(__name__)
CORS(app)  # enable cross-origin requests

# register blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(cart_bp, url_prefix="/cart")
app.register_blueprint(orders_bp, url_prefix="/orders")
app.register_blueprint(messages_bp, url_prefix="/messages")

@app.route("/")
def home():
    return {"message": "Backend API is running 🚀"}

if __name__ == "_main_":
    app.run(debug=True)