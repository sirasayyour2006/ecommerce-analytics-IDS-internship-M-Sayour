# Data Understanding Report

## Project Dataset

The project uses the Olist Brazilian E-Commerce dataset.  
This report summarizes the initial understanding of the main datasets required for Week 1:

- Customers
- Orders
- Order Items
- Products

The objective of this step is to understand the dataset structure, identify primary keys and relationships, and document initial data quality issues before cleaning and transformation.

---

## 1. Customers Dataset

**File:** `olist_customers_dataset.csv`

### Structure

- Number of rows: 99,441
- Number of columns: 5

### Columns

- `customer_id`
- `customer_unique_id`
- `customer_zip_code_prefix`
- `customer_city`
- `customer_state`

### Data Types

- `customer_id`: string
- `customer_unique_id`: string
- `customer_zip_code_prefix`: integer
- `customer_city`: string
- `customer_state`: string

### Primary Key

- `customer_id`

### Data Quality Findings

- Missing values: No missing values found.
- Duplicate rows: 0 duplicate rows.
- City and state fields should be standardized for consistency.
- `customer_city` should be converted to title case.
- `customer_state` should be converted to uppercase.

---

## 2. Orders Dataset

**File:** `olist_orders_dataset.csv`

### Structure

- Number of rows: 99,441
- Number of columns: 8

### Columns

- `order_id`
- `customer_id`
- `order_status`
- `order_purchase_timestamp`
- `order_approved_at`
- `order_delivered_carrier_date`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

### Data Types

All columns were initially loaded as strings.

### Primary Key

- `order_id`

### Foreign Key

- `customer_id`

### Data Quality Findings

Missing values were found in some date columns:

- `order_approved_at`: 160 missing values
- `order_delivered_carrier_date`: 1,783 missing values
- `order_delivered_customer_date`: 2,965 missing values

Other findings:

- Duplicate rows: 0 duplicate rows.
- Date columns need to be converted to datetime format.
- Only delivered orders should be kept for delivery performance analysis.
- Delivery metrics should be created, such as:
  - `order_date`
  - `delivery_date`
  - `delivery_days`
  - `is_delayed`

---

## 3. Order Items Dataset

**File:** `olist_order_items_dataset.csv`

### Structure

- Number of rows: 112,650
- Number of columns: 7

### Columns

- `order_id`
- `order_item_id`
- `product_id`
- `seller_id`
- `shipping_limit_date`
- `price`
- `freight_value`

### Data Types

- `order_id`: string
- `order_item_id`: integer
- `product_id`: string
- `seller_id`: string
- `shipping_limit_date`: string
- `price`: float
- `freight_value`: float

### Primary Key

The dataset uses a composite key:

- `order_id`
- `order_item_id`

### Foreign Keys

- `order_id`
- `product_id`
- `seller_id`

### Data Quality Findings

- Missing values: No missing values found.
- Duplicate rows: 0 duplicate rows.
- `shipping_limit_date` should be converted to datetime if needed.
- Revenue can be calculated at item level using:

```text
item_revenue = price + freight_value