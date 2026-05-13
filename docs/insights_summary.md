# Business Insights Summary

## Project Title

E-commerce Analytics Dashboard

## Business Problem

The company operates an online marketplace and needs a reliable analytics solution to monitor sales performance, product performance, regional contribution, and delivery efficiency.

The business needs to answer key questions such as:

- What is the total revenue?
- How many orders were completed?
- What is the average order value?
- Which product categories generate the most revenue?
- Which regions contribute the most to sales?
- What percentage of orders are delayed or delivered on time?

---

## Data Approach

The project followed an end-to-end analytics workflow:

1. Downloaded the Olist E-commerce dataset using the Kaggle API.
2. Cleaned and transformed the required datasets using Python and Pandas.
3. Loaded processed datasets into SQLite staging tables.
4. Built a SQL star schema.
5. Connected Power BI to the SQL model.
6. Built executive dashboards and extracted business insights.

The final dashboard uses the following analytics tables:

- `fact_orders`
- `dim_customers`
- `dim_products`
- `dim_date`

---

# Dashboard Overview

The Power BI report contains four pages:

1. Sales Overview
2. Product Performance
3. Regional Performance
4. Delivery Performance

---

# Key Business Insights

## 1. Sales Overview Insights

The Sales Overview dashboard shows the main sales performance indicators.

### Main KPIs

- Total Revenue: 15.42M
- Orders: 96K
- Average Order Value: 159.83
- Average Delivery Days: 12.01 days

### Interpretation

The business generated approximately 15.42M in total revenue from about 96K completed orders.

The Average Order Value is 159.83, which means that each completed order generates around 160 in revenue on average.

The average delivery time is 12.01 days, which provides an important operational benchmark for evaluating delivery performance.

The monthly revenue trend shows that revenue performance changes over time. This trend helps management monitor business growth, detect weaker months, and investigate possible seasonality or operational issues.

### Business Meaning

Sales KPIs give management a clear view of business performance. Monitoring total revenue, order volume, and AOV helps identify whether growth is driven by more orders, higher order value, or both.

---

## 2. Product Performance Insights

The Product Performance dashboard shows revenue distribution by product category and top products.

### Top-Performing Categories

The highest revenue-generating categories include:

1. beleza_saude
2. relogios_presentes
3. cama_mesa_banho
4. esporte_lazer
5. informatica_acessorios

### Interpretation

The category `beleza_saude` appears to be the strongest product category by revenue, followed by `relogios_presentes` and `cama_mesa_banho`.

These categories are key revenue drivers for the business and should receive more focus in marketing, inventory planning, and supplier management.

### Top Products

The Top Products visual shows that a small number of products generate significantly higher revenue than others. The top products range approximately between 40K and 67K in revenue.

### Business Meaning

High-performing categories and products should be prioritized because they contribute strongly to total revenue. The company can use these insights to improve stock planning, marketing campaigns, and product recommendations.

---

## 3. Regional Performance Insights

The Regional Performance dashboard shows revenue distribution by customer location.

### Top-Performing States

The highest revenue-generating states are:

1. SP
2. RJ
3. MG
4. RS
5. PR

### Interpretation

SP is the strongest state by revenue and contributes much more than other states. RJ and MG also show strong performance, but there is a large gap between SP and the rest of the states.

This suggests that revenue is geographically concentrated in a few major regions.

### Underperforming Regions

The lowest-performing states include:

- RR
- AP
- AC
- AM
- RO
- TO

These regions generate much lower revenue compared to the top states.

### Business Meaning

The company should continue investing in high-performing regions such as SP, RJ, and MG while also investigating why some regions are underperforming.

Underperforming regions may have lower customer demand, weaker marketing reach, delivery limitations, or lower product availability.

---

## 4. Delivery Performance Insights

The Delivery Performance dashboard compares delayed orders with on-time orders.

### Main Delivery KPIs

- On-time orders: 89K
- On-time percentage: 91.89%
- Delayed orders: 8K
- Delayed percentage: 8.11%
- Average delivery days: 12.01 days

### Interpretation

Most orders are delivered on time. Around 91.89% of orders are on time, while 8.11% are delayed.

This indicates that the delivery process is generally performing well, but delayed orders still represent a meaningful operational issue.

The delivery days trend shows changes in average delivery time over time. A decreasing delivery duration trend may indicate operational improvement, better logistics, or changes in delivery coverage.

### Business Meaning

Delivery performance directly affects customer satisfaction. Even though the on-time percentage is high, the company should continue monitoring delayed orders and work to reduce the delayed percentage further.

---

# Strategic Recommendations

## 1. Monitor Revenue and Orders Monthly

The company should track total revenue, order count, and AOV on a monthly basis.

Recommended actions:

- Monitor monthly revenue trends.
- Investigate months with revenue drops.
- Compare order growth with revenue growth.
- Track AOV to understand customer spending behavior.

---

## 2. Focus on High-Performing Product Categories

The company should prioritize categories that generate the highest revenue.

Recommended actions:

- Increase marketing campaigns for top categories.
- Ensure strong inventory availability for best-selling categories.
- Strengthen supplier relationships for high-performing products.
- Use top categories in promotional campaigns and homepage recommendations.

---

## 3. Review Low-Performing Product Categories

Low-performing categories should be analyzed to understand why they generate less revenue.

Recommended actions:

- Review pricing strategy.
- Improve product visibility.
- Test promotional campaigns.
- Consider replacing or reducing focus on weak categories.

---

## 4. Strengthen Regional Strategy

Revenue is concentrated in major states, especially SP, RJ, and MG.

Recommended actions:

- Maintain strong customer retention campaigns in top-performing states.
- Launch targeted marketing campaigns in underperforming regions.
- Study regional customer behavior.
- Improve delivery coverage in weaker regions.
- Evaluate whether delivery delays or logistics costs affect regional performance.

---

## 5. Improve Delivery Performance

Although most orders are delivered on time, delayed orders still represent 8.11% of total orders.

Recommended actions:

- Track delayed orders by region.
- Identify carriers or areas with frequent delays.
- Review estimated delivery dates.
- Improve logistics partnerships.
- Monitor delivery performance as a regular operational KPI.

---

# Final Conclusion

The Power BI dashboard provides an executive-level view of e-commerce performance.

The business generated 15.42M in revenue from 96K orders, with an Average Order Value of 159.83. Product revenue is driven mainly by categories such as beleza_saude, relogios_presentes, and cama_mesa_banho. Regionally, SP is the strongest revenue contributor, followed by RJ and MG. Delivery performance is generally strong, with 91.89% of orders delivered on time and 8.11% delayed.

Overall, the dashboard helps management monitor sales, product performance, regional contribution, and delivery efficiency. The insights can support better decisions in marketing, inventory planning, regional strategy, and logistics improvement.
