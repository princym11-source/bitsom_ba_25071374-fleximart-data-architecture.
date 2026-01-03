-- Query 1: Monthly Sales Drill-Down
SELECT
    d.year,
    d.quarter,
    d.month_name,
    SUM(f.total_amount) AS total_sales,
    SUM(f.quantity_sold) AS total_quantity
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.year, d.quarter, d.month_name
ORDER BY d.year, d.quarter;

-- Query 2: Top Products by Revenue
SELECT
    p.product_name,
    p.category,
    SUM(f.quantity_sold) AS units_sold,
    SUM(f.total_amount) AS revenue,
    (SUM(f.total_amount) / (SELECT SUM(total_amount) FROM fact_sales)) * 100 AS revenue_percentage
FROM fact_sales f
JOIN dim_product p ON f.product_key = p.product_key
GROUP BY p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;

-- Query 3: Customer Segmentation
WITH customer_totals AS (
    SELECT
        customer_key,
        SUM(total_amount) AS total_spent
    FROM fact_sales
    GROUP BY customer_key
)
SELECT
    CASE
        WHEN total_spent > 50000 THEN 'High Value'
        WHEN total_spent BETWEEN 20000 AND 50000 THEN 'Medium Value'
        ELSE 'Low Value'
    END AS customer_segment,
    COUNT(*) AS customer_count,
    SUM(total_spent) AS total_revenue,
    AVG(total_spent) AS avg_revenue
FROM customer_totals
GROUP BY customer_segment;
