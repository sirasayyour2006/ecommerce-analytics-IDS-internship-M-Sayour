# Business Insights Summary

## Project Title

E-commerce Analytics Dashboard

## Business Problem

The company operates an online marketplace with transactional data stored in raw CSV files.  
Management needs a reliable analytics solution to monitor sales performance, product performance, regional contribution, and delivery efficiency.

Before this project, the business lacked:
- Standardized KPIs
- Clean reporting tables
- A centralized analytics model
- Executive dashboards for decision-making

---

## Data Approach

The project followed an end-to-end analytics workflow:

1. Downloaded the Olist E-commerce dataset using the Kaggle API.
2. Cleaned and transformed the required datasets using Python and Pandas.
3. Loaded processed datasets into SQLite staging tables.
4. Built a star schema using SQL.
5. Created Power BI dashboards using the analytics-ready model.
6. Developed business insights and recommendations based on dashboard results.

The final Power BI model used the following tables:

- `fact_orders`
- `dim_customers`
- `dim_products`
- `dim_date`

---

## Dashboard Pages

The Power BI report contains four executive dashboard pages:

1. **Sales Overview**
   - Total Revenue
   - Orders
   - Average Order Value
   - Monthly Revenue Trend

2. **Product Performance**
   - Revenue by Product Category
   - Top Products by Revenue

3. **Regional Performance**
   - Revenue by State
   - Top Cities by Revenue

4. **Delivery Performance**
   - Delayed vs On-Time Orders
   - Delayed Percentage
   - On-Time Percentage

---

# Key Business Insights

## 1. Sales Overview Insights

The Sales Overview dashboard shows the overall sales performance of the business.

Key observations:

- Total Revenue provides a clear view of the revenue generated from delivered orders.
- Orders show the number of unique completed orders.
- Average Order Value helps understand how much revenue is generated per order on average.
- The monthly revenue trend shows changes in business performance over time.

Business interpretation:

Revenue trends help management identify strong and weak sales periods.  
If revenue decreases in certain months, the business should investigate possible causes such as lower demand, product availability, seasonal effects, or delivery issues.

---

## 2. Product Performance Insights

The Product Performance dashboard identifies which product categories and products generate the highest revenue.

Key observations:

- Some product categories contribute significantly more revenue than others.
- The Top 10 products represent the strongest revenue-generating products.
- Product categories with low revenue may need further investigation.

Business interpretation:

High-performing categories should receive more marketing focus, better inventory planning, and stronger supplier relationships.  
Low-performing categories may need pricing review, promotional campaigns, or product portfolio evaluation.

---

## 3. Regional Performance Insights

The Regional Performance dashboard shows how revenue is distributed by customer location.

Key observations:

- Some states generate much higher revenue than others.
- Top cities contribute strongly to overall sales.
- Underperforming regions may represent growth opportunities.

Business interpretation:

Regional revenue differences can help the company improve location-based marketing strategies.  
High-performing regions can be prioritized for customer retention campaigns, while underperforming regions can be targeted with promotions, logistics improvements, or market research.

---

## 4. Delivery Performance Insights

The Delivery Performance dashboard compares delayed orders with on-time orders.

Key observations:

- Orders are classified as either delayed or on time.
- Delayed Percentage measures the share of orders delivered after the estimated delivery date.
- On-Time Percentage measures the share of orders delivered on or before the estimated date.

Business interpretation:

Delivery performance directly affects customer satisfaction.  
A high delayed percentage may indicate logistics inefficiencies, carrier issues, or unrealistic estimated delivery dates.

---

# Strategic Recommendations

## 1. Improve Sales Monitoring

The company should monitor revenue, orders, and AOV regularly to detect performance changes early.

Recommended actions:
- Track monthly revenue trends.
- Compare performance across months.
- Investigate sudden drops in revenue or order count.

---

## 2. Focus on High-Performing Categories

The company should prioritize product categories that generate the highest revenue.

Recommended actions:
- Increase marketing campaigns for top categories.
- Ensure stock availability for high-demand products.
- Build stronger supplier relationships for best-selling categories.

---

## 3. Review Low-Performing Products and Categories

Underperforming categories should be reviewed to understand why they generate lower revenue.

Recommended actions:
- Analyze pricing strategy.
- Review product visibility.
- Create promotional campaigns.
- Consider removing or replacing weak products.

---

## 4. Strengthen Regional Strategy

The company should use regional insights to improve market targeting.

Recommended actions:
- Invest more in high-performing states and cities.
- Create localized campaigns for underperforming regions.
- Study customer behavior by region.
- Improve delivery coverage in weaker regions.

---

## 5. Improve Delivery Performance

Delivery performance should be continuously monitored because it affects customer satisfaction.

Recommended actions:
- Identify regions with high delay rates.
- Work with logistics partners to reduce delays.
- Review estimated delivery dates.
- Monitor delayed orders as a regular operational KPI.

---

# Final Conclusion

The Power BI dashboard provides an executive-level view of e-commerce performance.

It helps answer important business questions such as:

- How much revenue is the business generating?
- How many orders were completed?
- What is the average order value?
- Which product categories perform best?
- Which products generate the highest revenue?
- Which regions contribute most to sales?
- What percentage of orders are delayed or delivered on time?

The project successfully transformed raw e-commerce data into a clean, analytics-ready SQL model and an executive Power BI dashboard that supports business decision-making.
