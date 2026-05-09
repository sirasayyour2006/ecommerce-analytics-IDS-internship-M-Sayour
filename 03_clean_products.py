import pandas as pd
import os

RAW_PATH = "data/raw/olist_products_dataset.csv"
OUTPUT_PATH = "data/processed/products_clean.csv"

os.makedirs("data/processed", exist_ok=True)

products = pd.read_csv(RAW_PATH)

print("Before cleaning:", products.shape)

products["product_category_name"] = (
    products["product_category_name"]
    .fillna("unknown")
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
)

products = products.drop_duplicates(subset=["product_id"])

print("After cleaning:", products.shape)

products.to_csv(OUTPUT_PATH, index=False)

print(f"Saved cleaned products to {OUTPUT_PATH}")