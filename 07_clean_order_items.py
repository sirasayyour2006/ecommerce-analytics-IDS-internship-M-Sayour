import pandas as pd
import os

RAW_PATH = "data/raw/olist_order_items_dataset.csv"
OUTPUT_PATH = "data/processed/order_items_clean.csv"

os.makedirs("data/processed", exist_ok=True)

order_items = pd.read_csv(RAW_PATH)

print("Before cleaning:", order_items.shape)

order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"],
    errors="coerce"
)

order_items["item_revenue"] = order_items["price"] + order_items["freight_value"]

order_items = order_items.drop_duplicates(
    subset=["order_id", "order_item_id"]
)

print("After cleaning:", order_items.shape)

order_items.to_csv(OUTPUT_PATH, index=False)

print(f"Saved cleaned order items to {OUTPUT_PATH}")