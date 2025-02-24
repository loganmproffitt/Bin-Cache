import random
import psycopg2
import os
import csv
from faker import Faker

fake = Faker()

# Connect to Postgres
conn = psycopg2.connect(dbname="fulfillment", user="loganproffitt", password="1260", host="localhost")
cur = conn.cursor()

# Set counts
order_count = 5000
max_order_items = 10
max_items = 5

# Load items from CSV
item_ids = []
item_prices = []  # Store prices to reference later

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_path = os.path.join(script_dir, '../data/items.csv')

# Open the CSV file
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        item_name = row['name']
        item_description = row['description']
        item_price = float(row['price'])

        # Insert item
        cur.execute("""
            INSERT INTO items (name, description, price, created_at)
            VALUES (%s, %s, %s, NOW()) RETURNING id
        """, (item_name, item_description, item_price))

        item_id = cur.fetchone()[0]  # Get the generated item id
        item_ids.append(item_id)  # Store item_id
        item_prices.append(item_price)  # Store the corresponding item price

# Generate orders
order_ids = []
for _ in range(order_count):
    order_status = random.choice(['pending', 'canceled', 'in transit', 'complete'])
    created_at = fake.date_this_year()  # Random creation date
    updated_at = fake.date_this_year()  # Random update date

    cur.execute("""
        INSERT INTO orders (status, created_at, updated_at)
        VALUES (%s, %s, %s) RETURNING id
    """, (order_status, created_at, updated_at))

    order_id = cur.fetchone()[0]  # Get generated order_id
    order_ids.append(order_id)  # Store order_id

# Generate order_items
for order_id in order_ids:
    item_count = random.randint(1, max_order_items)  # Add random number of items
    for _ in range(item_count):
        item_id = random.choice(item_ids)  # Pick a random item
        quantity = random.randint(1, max_items)  # Random quantity
        item_price = item_prices[item_ids.index(item_id)]  # Get the price from item_prices list

        cur.execute("""
            INSERT INTO order_items (order_id, item_id, quantity, price_at_purchase)
            VALUES (%s, %s, %s, %s)
        """, (order_id, item_id, quantity, item_price))  # Use item_price directly

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
