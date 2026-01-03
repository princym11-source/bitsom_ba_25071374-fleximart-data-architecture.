import pandas as pd
import mysql.connector
from datetime import datetime

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="fleximart"
)
cursor = conn.cursor()

# ---------------- REPORT METRICS ----------------
report = {
    "customers_processed": 0,
    "customers_loaded": 0,
    "customer_duplicates_removed": 0,
    "customers_missing_email": 0,

    "products_processed": 0,
    "products_loaded": 0,
    "products_missing_price": 0,
    "products_missing_stock": 0,

    "sales_processed": 0,
    "sales_loaded": 0,
    "sales_duplicates_removed": 0,
    "sales_missing_ids": 0
}

# ---------------- HELPER FUNCTIONS ----------------
def standardize_phone(phone):
    if pd.isna(phone):
        return None
    digits = ''.join(filter(str.isdigit, phone))
    return f"+91-{digits[-10:]}" if len(digits) >= 10 else None

def parse_date(date_value):
    try:
        return pd.to_datetime(date_value, dayfirst=True).date()
    except:
        return None

# ===================================================
#                  CUSTOMERS ETL
# ===================================================
customers = pd.read_csv("../data/customers_raw.csv")
report["customers_processed"] = len(customers)

customers.drop_duplicates(subset=["customer_id"], inplace=True)
report["customer_duplicates_removed"] = report["customers_processed"] - len(customers)

customers_missing_email = customers["email"].isna().sum()
report["customers_missing_email"] = customers_missing_email

customers = customers.dropna(subset=["email"])

customers["phone"] = customers["phone"].apply(standardize_phone)
customers["registration_date"] = customers["registration_date"].apply(parse_date)
customers["city"] = customers["city"].str.title()

for _, row in customers.iterrows():
    cursor.execute("""
        INSERT INTO customers (first_name, last_name, email, phone, city, registration_date)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (
        row["first_name"].strip(),
        row["last_name"].strip(),
        row["email"].strip(),
        row["phone"],
        row["city"],
        row["registration_date"]
    ))

report["customers_loaded"] = len(customers)

# ===================================================
#                  PRODUCTS ETL
# ===================================================
products = pd.read_csv("../data/products_raw.csv")
report["products_processed"] = len(products)

products["category"] = products["category"].str.strip().str.title()
products["product_name"] = products["product_name"].str.strip()

missing_price = products["price"].isna().sum()
report["products_missing_price"] = missing_price
products["price"].fillna(products["price"].median(), inplace=True)

missing_stock = products["stock_quantity"].isna().sum()
report["products_missing_stock"] = missing_stock
products["stock_quantity"].fillna(0, inplace=True)

for _, row in products.iterrows():
    cursor.execute("""
        INSERT INTO products (product_name, category, price, stock_quantity)
        VALUES (%s, %s, %s, %s)
    """, (
        row["product_name"],
        row["category"],
        row["price"],
        int(row["stock_quantity"])
    ))

report["products_loaded"] = len(products)

# ===================================================
#                    SALES ETL
# ===================================================
sales = pd.read_csv("../data/sales_raw.csv")
report["sales_processed"] = len(sales)

sales.drop_duplicates(subset=["transaction_id"], inplace=True)
report["sales_duplicates_removed"] = report["sales_processed"] - len(sales)

missing_ids = sales["customer_id"].isna().sum() + sales["product_id"].isna().sum()
report["sales_missing_ids"] = missing_ids

sales = sales.dropna(subset=["customer_id", "product_id"])
sales["transaction_date"] = sales["transaction_date"].apply(parse_date)

for _, row in sales.iterrows():
    cursor.execute("""
        INSERT INTO orders (customer_id, order_date, total_amount, status)
        VALUES (
            (SELECT customer_id FROM customers WHERE email IS NOT NULL LIMIT 1),
            %s,
            %s,
            %s
        )
    """, (
        row["transaction_date"],
        row["quantity"] * row["unit_price"],
        row["status"]
    ))

report["sales_loaded"] = len(sales)

# ---------------- FINALIZE ----------------
conn.commit()
conn.close()

# ---------------- WRITE REPORT ----------------
with open("data_quality_report.txt", "w") as f:
    f.write("FlexiMart ETL Data Quality Report\n")
    f.write("--------------------------------\n")
    for key, value in report.items():
        f.write(f"{key.replace('_', ' ').title()}: {value}\n")
