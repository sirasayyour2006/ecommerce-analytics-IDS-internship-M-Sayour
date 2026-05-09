import pandas as pd
import os

ORDER_ITEMS_PATH = "data/raw/olist_order_items_dataset.csv"
ORDERS_CLEAN_PATH = "data/processed/orders_clean.csv"
OUTPUT_PATH = "data/processed/orders_revenue_enriched.csv"

os.makedirs("data/processed", exist_ok=True)

order_items = pd.read_csv(ORDER_ITEMS_PATH)
orders = pd.read_csv(ORDERS_CLEAN_PATH)

print("Order items shape:", order_items.shape)
print("Orders clean shape:", orders.shape)

order_items["item_revenue"] = order_items["price"] + order_items["freight_value"]

order_revenue = (
    order_items
    .groupby("order_id", as_index=False)
    .agg(
        total_price=("price", "sum"),
        total_freight=("freight_value", "sum"),
        total_revenue=("item_revenue", "sum"),
        total_items=("order_item_id", "count")
    )
)

orders_revenue = orders.merge(order_revenue, on="order_id", how="left")

orders_revenue["total_price"] = orders_revenue["total_price"].fillna(0)
orders_revenue["total_freight"] = orders_revenue["total_freight"].fillna(0)
orders_revenue["total_revenue"] = orders_revenue["total_revenue"].fillna(0)
orders_revenue["total_items"] = orders_revenue["total_items"].fillna(0).astype(int)

print("Revenue enriched shape:", orders_revenue.shape)

orders_revenue.to_csv(OUTPUT_PATH, index=False)

print(f"Saved revenue enriched orders to {OUTPUT_PATH}")