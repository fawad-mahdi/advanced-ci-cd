# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    try:
        # Retrieve numbers from query parameters
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return jsonify({"result": result})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input"}), 400

if __name__ == "__main__":
    app.run(debug=True)
