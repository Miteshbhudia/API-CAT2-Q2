# REST API for Product Management Q2 

# Overview of the system 
This project provides a simple REST API built with Flask for managing products. It allows users to create and retrieve product information.

# A. Setup Instructions

# 1. Install dependencies:
pip install flask requests

# 2. Start the API server:
python app.py

# 3. Test the API:
Execute the client.py script to interact with the API:
python client.py

# B. API ENDPOINTS
# 1. POST /products

# Functionality: Adds a new product to the system.
# Request Body (JSON Format):

{
    "name": "Product Name",
    "description": "Product Description",
    "price": 10.5
}

# C. Handling Requests and Responses:
201 Created: Returns the details of the created product.
400 Bad Request: Indicates invalid input.

# 2. GET /products
# Functionality: Retrieves a list of all available products.
# Responses:
200 OK: Returns an array of products in JSON format.

# D. Client Script
The client.py script demonstrates how to interact with the API. It includes examples for:

Creating products using the /products endpoint.
Fetching all products from the server.


