ENTITY: customers
Purpose: Stores customer information.
Attributes:
- customer_id (PK)
- first_name
- last_name
- email
- phone
- city
- registration_date

Relationships:
One customer can place many orders.

ENTITY: products
Purpose: Stores product details.
Attributes:
- product_id (PK)
- product_name
- category
- price
- stock_quantity

ENTITY: orders
Purpose: Stores order-level information.
Attributes:
- order_id (PK)
- customer_id (FK)
- order_date
- total_amount
- status

ENTITY: order_items
Purpose: Stores individual order items.
Attributes:
- order_item_id (PK)
- order_id (FK)
- product_id (FK)
- quantity
- unit_price
- subtotal

Normalization Explanation:
The schema follows Third Normal Form (3NF). All non-key attributes depend only on the primary key. Customer, product, and order data are separated to avoid redundancy. This design prevents update, insert, and delete anomalies while maintaining referential integrity.
