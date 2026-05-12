# KPI Definitions

## Dashboard Overview

This document provides a brief explanation of the KPIs and visuals used in the Power BI dashboard for the E-commerce Analytics Project.

The dashboard was built using the SQL star schema created in Week 2.

Main tables used:
- `fact_orders`
- `dim_customers`
- `dim_products`
- `dim_date`

The Power BI report contains four pages:
1. Sales Overview
2. Product Performance
3. Regional Performance
4. Delivery Performance

---

## 1. Sales Overview Dashboard

The Sales Overview page summarizes the main business performance indicators.

### Total Revenue

**Definition:**  
Total Revenue represents the total amount generated from delivered orders.

**DAX Formula:**

```DAX
Total Revenue = SUM(fact_orders[item_revenue])
