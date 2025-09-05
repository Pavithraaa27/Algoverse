from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample endpoint (replace with your logic)
@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"message": "Hello from Hackathon backend!"})

# Example: mock business logic
@app.route("/api/expenses", methods=["POST"])
def add_expense():
    data = request.json
    return jsonify({
        "status": "success",
        "expense": data
    })

if __name__ == "__main__":
    app.run(debug=True)