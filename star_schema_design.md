FACT TABLE: fact_sales

Grain:
One record per product per order line item.

Business Process:
Sales transactions generated from customer orders.

Measures:
- quantity_sold: Number of units sold
- unit_price: Price per unit at the time of sale
- discount_amount: Discount applied on the sale
- total_amount: Final sale value after discount

Foreign Keys:
- date_key → dim_date
- product_key → dim_product
- customer_key → dim_customer

DIMENSION TABLE: dim_date

Purpose:
Provides time-based analysis for reporting and trends.

Attributes:
- date_key (PK): Surrogate key in YYYYMMDD format
- full_date: Actual calendar date
- day_of_week: Day name
- day_of_month: Numeric day
- month: Month number
- month_name: Month name
- quarter: Q1, Q2, Q3, Q4
- year: Calendar year
- is_weekend: Boolean flag

DIMENSION TABLE: dim_product

Purpose:
Stores descriptive information about products.

Attributes:
- product_key (PK)
- product_id
- product_name
- category
- subcategory
- unit_price

DIMENSION TABLE: dim_customer

Purpose:
Stores customer demographic information.

Attributes:
- customer_key (PK)
- customer_id
- customer_name
- city
- state
- customer_segment

Design Decisions:
The chosen granularity allows detailed analysis at the transaction level. Surrogate keys ensure historical accuracy and isolate the warehouse from changes in source systems. The star schema enables efficient drill-down and roll-up operations across time, product, and customer dimensions.
