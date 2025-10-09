# generate_products.py
import csv
import random
import os

PRODUCT_NAMES = [
    "Laptop","Phone","Tablet","Headphones","Keyboard","Mouse","Charger",
    "Monitor","Speaker","Camera","Smartwatch","Router","SSD","Printer"
]
ADJECTIVES = ["Pro","Plus","Mini","Ultra","Air","Max","X","S","Neo","Prime"]
CATEGORIES = ["Electronics","Accessories","Gadgets","Computers","Audio","Networking","Storage"]
SUPPLIERS = ["TechWorld","GadgetZone","SmartMart","ElectroHub","TechieStore","PrimeSupplies"]
DESCRIPTIONS = [
    "High quality","Value for money","Latest model","Compact and powerful",
    "Long battery life","Ergonomic design","Best seller","Limited edition"
]

def make_product_name():
    return f"{random.choice(PRODUCT_NAMES)} {random.choice(ADJECTIVES)} {random.randint(100,999)}"

def generate(filename='products.csv', n=10000, corrupt=False, corrupt_rate=0.001):
    # corrupt=True will create a small fraction of rows with missing column to test error handling
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['product_id','product_name','category','price','stock_quantity','supplier','rating','description'])
        for i in range(1, n+1):
            name = make_product_name()
            category = random.choice(CATEGORIES)
            supplier = random.choice(SUPPLIERS)
            price = round(random.uniform(199.0, 99999.99), 2)
            stock = random.randint(0, 2000)
            rating = round(random.uniform(1.0, 5.0), 1)
            desc = random.choice(DESCRIPTIONS)
            row = [i, name, category, price, stock, supplier, rating, desc]

            if corrupt and random.random() < corrupt_rate:
                # intentionally drop the description column (simulate a malformed row)
                writer.writerow(row[:-1])
            else:
                writer.writerow(row)

    print(f"✅ Created {filename} with {n} records (plus header).")

if __name__ == '__main__':
    # run with corrupt=True to add a few malformed rows
    generate(filename='products.csv', n=10000, corrupt=False)
