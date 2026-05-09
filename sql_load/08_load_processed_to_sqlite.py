import sqlite3
import pandas as pd
import os

PROCESSED_DIR = "data/processed"
DB_PATH = "data/ecommerce_analytics.db"

tables = {
    "stg_customers": "customers_clean.csv",
    "stg_products": "products_clean.csv",
    "stg_orders": "orders_clean.csv",
    "stg_order_revenue": "orders_revenue_enriched.csv",
    "stg_order_items": "order_items_clean.csv"
}

def load_csv_to_sqlite():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    for table_name, file_name in tables.items():
        file_path = os.path.join(PROCESSED_DIR, file_name)

        print(f"Loading {file_name} into {table_name}...")

        df = pd.read_csv(file_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)

        print(f"{table_name} loaded successfully. Rows: {len(df)}")

    conn.close()
    print("All processed CSV files were loaded into SQLite successfully.")

if __name__ == "__main__":
    load_csv_to_sqlite()