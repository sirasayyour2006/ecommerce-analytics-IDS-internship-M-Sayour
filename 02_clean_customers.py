import pandas as pd
import os

RAW_PATH = "data/raw/olist_customers_dataset.csv"
OUTPUT_PATH = "data/processed/customers_clean.csv"

os.makedirs("data/processed", exist_ok=True)

customers = pd.read_csv(RAW_PATH)

print("Before cleaning:", customers.shape)

customers["customer_city"] = customers["customer_city"].astype(str).str.strip().str.title()
customers["customer_state"] = customers["customer_state"].astype(str).str.strip().str.upper()

customers = customers.drop_duplicates(subset=["customer_id"])

print("After cleaning:", customers.shape)

customers.to_csv(OUTPUT_PATH, index=False)

print(f"Saved cleaned customers to {OUTPUT_PATH}")