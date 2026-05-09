import pandas as pd
import os

RAW_PATH = "data/raw/olist_orders_dataset.csv"
OUTPUT_PATH = "data/processed/orders_clean.csv"

os.makedirs("data/processed", exist_ok=True)

orders = pd.read_csv(RAW_PATH)

print("Before cleaning:", orders.shape)

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

orders = orders[orders["order_status"] == "delivered"].copy()

orders["order_date"] = orders["order_purchase_timestamp"].dt.date
orders["delivery_date"] = orders["order_delivered_customer_date"].dt.date

orders["delivery_days"] = (
    orders["order_delivered_customer_date"] - orders["order_purchase_timestamp"]
).dt.days

orders["is_delayed"] = (
    orders["order_delivered_customer_date"] > orders["order_estimated_delivery_date"]
)

orders = orders.drop_duplicates(subset=["order_id"])

print("After cleaning:", orders.shape)

orders.to_csv(OUTPUT_PATH, index=False)

print(f"Saved cleaned orders to {OUTPUT_PATH}")