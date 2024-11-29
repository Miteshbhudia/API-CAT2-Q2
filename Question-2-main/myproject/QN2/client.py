

import requests

BASE_URL = 'http://127.0.0.1:5000'

def add_product(name, description, price):
    payload = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(f"{BASE_URL}/products", json=payload)
    if response.status_code == 201:
        print("Product created:", response.json())
    else:
        print("Failed to create product:", response.json())

def list_products():
    response = requests.get(f"{BASE_URL}/products")
    if response.status_code == 200:
        print("Products:", response.json())
    else:
        print("Failed to retrieve products:", response.json())

# Example usage
if __name__ == "__main__":
    # Add products
    add_product("Product A", "Description A", 10.5)
    add_product("Product B", "Description B", 20.0)

    # List products
    list_products()