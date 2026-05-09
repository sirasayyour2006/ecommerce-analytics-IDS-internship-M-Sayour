import pandas as pd
import os

RAW_DIR = "data/raw"

files = {
    "customers": "olist_customers_dataset.csv",
    "orders": "olist_orders_dataset.csv",
    "order_items": "olist_order_items_dataset.csv",
    "products": "olist_products_dataset.csv"
}

for name, file in files.items():
    path = os.path.join(RAW_DIR, file)
    df = pd.read_csv(path)

    print("=" * 80)
    print(f"Dataset: {name}")
    print("=" * 80)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nPreview:")
    print(df.head())