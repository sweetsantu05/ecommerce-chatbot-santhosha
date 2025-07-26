from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def query_db(query):
    conn = sqlite3.connect('ecommerce.db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/')
def home():
    return "✅ API is running!"

@app.route('/products')
def get_products():
    rows = query_db("SELECT * FROM products")
    return jsonify(rows)

@app.route('/orders')
def get_orders():
    rows = query_db("SELECT * FROM orders")
    return jsonify(rows)

@app.route('/inventory')
def get_inventory():
    rows = query_db("SELECT * FROM inventory")
    return jsonify(rows)

if __name__ == '__main__':
    app.run(debug=True)
