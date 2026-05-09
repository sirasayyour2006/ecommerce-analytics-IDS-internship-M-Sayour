# Data Quality Report

## Project Dataset

This report documents the data quality validation performed during Week 1 of the E-commerce Analytics Internship Project.

The validation was performed after downloading, cleaning, and transforming the required Olist e-commerce datasets using Python and Pandas.

## Processed Datasets Validated

The following processed datasets were validated:

- `customers_clean.csv`
- `products_clean.csv`
- `orders_clean.csv`
- `orders_revenue_enriched.csv`

## Validation Objectives

The main validation checks included:

- Null checks
- Duplicate row checks
- Primary key duplicate checks
- Revenue validation
- Delivery validation

---

## 1. Customers Data Quality

### Dataset

`customers_clean.csv`

### Dataset Size

- Rows: 99,441
- Columns: 5

### Null Checks

No missing values were found in the customers dataset.

| Column | Missing Values |
|---|---:|
| customer_id | 0 |
| customer_unique_id | 0 |
| customer_zip_code_prefix | 0 |
| customer_city | 0 |
| customer_state | 0 |

### Duplicate Checks

- Duplicate rows: 0
- Duplicate `customer_id`: 0

### Cleaning Actions

- Removed extra spaces from city and state fields.
- Converted `customer_city` to title case.
- Converted `customer_state` to uppercase.
- Removed duplicate records based on `customer_id`.

### Result

The customers dataset is clean and ready for analysis.

---

## 2. Products Data Quality

### Dataset

`products_clean.csv`

### Dataset Size

- Rows: 32,951
- Columns: 9

### Null Checks

| Column | Missing Values |
|---|---:|
| product_id | 0 |
| product_category_name | 0 |
| product_name_lenght | 610 |
| product_description_lenght | 610 |
| product_photos_qty | 610 |
| product_weight_g | 2 |
| product_length_cm | 2 |
| product_height_cm | 2 |
| product_width_cm | 2 |

### Duplicate Checks

- Duplicate rows: 0
- Duplicate `product_id`: 0

### Cleaning Actions

- Replaced missing `product_category_name` values with `unknown`.
- Removed extra spaces from product category values.
- Converted product categories to lowercase.
- Standardized categories using underscores.
- Removed duplicate records based on `product_id`.

### Notes

Some descriptive and measurement columns still contain missing values. These fields are not required for the Week 1 revenue and KPI calculations, so they were kept for now instead of being removed or imputed.

### Result

The products dataset is suitable for product category analysis after category normalization.

---

## 3. Orders Data Quality

### Dataset

`orders_clean.csv`

### Dataset Size

- Rows: 96,478
- Columns: 12

### Null Checks

| Column | Missing Values |
|---|---:|
| order_id | 0 |
| customer_id | 0 |
| order_status | 0 |
| order_purchase_timestamp | 0 |
| order_approved_at | 14 |
| order_delivered_carrier_date | 2 |
| order_delivered_customer_date | 8 |
| order_estimated_delivery_date | 0 |
| order_date | 0 |
| delivery_date | 8 |
| delivery_days | 8 |
| is_delayed | 0 |

### Duplicate Checks

- Duplicate rows: 0
- Duplicate `order_id`: 0

### Cleaning Actions

- Converted timestamp columns to datetime format.
- Filtered orders to keep delivered orders only.
- Created `order_date`.
- Created `delivery_date`.
- Created `delivery_days`.
- Created `is_delayed`.
- Removed duplicate records based on `order_id`.

### Notes

There are 8 records with missing delivery dates and missing delivery duration even after filtering delivered orders. These records should be reviewed later before final dashboard reporting, especially for delivery performance analysis.

### Result

The orders dataset is mostly clean and ready for analysis, with a small number of delivery-date issues documented.

---

## 4. Revenue-Enriched Orders Data Quality

### Dataset

`orders_revenue_enriched.csv`

### Dataset Size

- Rows: 96,478
- Columns: 16

### Null Checks

| Column | Missing Values |
|---|---:|
| order_id | 0 |
| customer_id | 0 |
| order_status | 0 |
| order_purchase_timestamp | 0 |
| order_approved_at | 14 |
| order_delivered_carrier_date | 2 |
| order_delivered_customer_date | 8 |
| order_estimated_delivery_date | 0 |
| order_date | 0 |
| delivery_date | 8 |
| delivery_days | 8 |
| is_delayed | 0 |
| total_price | 0 |
| total_freight | 0 |
| total_revenue | 0 |
| total_items | 0 |

### Duplicate Checks

- Duplicate rows: 0
- Duplicate `order_id`: 0

### Revenue Validation

| Check | Result |
|---|---:|
| Negative `total_revenue` | 0 |
| Null `total_revenue` | 0 |

### Revenue Calculation Logic

Item-level revenue was calculated as:

```text
item_revenue = price + freight_value