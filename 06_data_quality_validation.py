import pandas as pd

customers = pd.read_csv("data/processed/customers_clean.csv")
products = pd.read_csv("data/processed/products_clean.csv")
orders = pd.read_csv("data/processed/orders_clean.csv")
revenue = pd.read_csv("data/processed/orders_revenue_enriched.csv")

print("=" * 80)
print("DATA QUALITY VALIDATION")
print("=" * 80)

checks = {
    "customers_clean": customers,
    "products_clean": products,
    "orders_clean": orders,
    "orders_revenue_enriched": revenue
}

for name, df in checks.items():
    print(f"\nDataset: {name}")
    print("Rows:", df.shape[0])
    print("Columns:", df.shape[1])
    print("Missing values:")
    print(df.isnull().sum())
    print("Duplicate rows:", df.duplicated().sum())

print("\nPrimary Key Checks:")
print("Duplicate customer_id:", customers["customer_id"].duplicated().sum())
print("Duplicate product_id:", products["product_id"].duplicated().sum())
print("Duplicate order_id in orders:", orders["order_id"].duplicated().sum())
print("Duplicate order_id in revenue:", revenue["order_id"].duplicated().sum())

print("\nRevenue Validation:")
print("Negative total_revenue:", (revenue["total_revenue"] < 0).sum())
print("Null total_revenue:", revenue["total_revenue"].isnull().sum())

print("\nDelivery Validation:")
print("Negative delivery_days:", (orders["delivery_days"] < 0).sum())
print("Null delivery_days:", orders["delivery_days"].isnull().sum())
print("Delayed orders:", orders["is_delayed"].sum())
print("On-time orders:", (~orders["is_delayed"]).sum())