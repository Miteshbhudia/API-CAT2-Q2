from django.apps import AppConfig


from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for products
products = []

@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        # Validate input
        if not all(k in data for k in ("name", "description", "price")):
            return jsonify({"error": "Missing fields"}), 400
        if not isinstance(data['price'], (int, float)):
            return jsonify({"error": "Invalid price format"}), 400

        product = {
            "id": len(products) + 1,
            "name": data["name"],
            "description": data["description"],
            "price": data["price"]
        }
        products.append(product)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)


