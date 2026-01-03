INSERT INTO dim_date VALUES
(20240115,'2024-01-15','Monday',15,1,'January','Q1',2024,false),
(20240201,'2024-02-01','Thursday',1,2,'February','Q1',2024,false),
(20240301,'2024-03-01','Friday',1,3,'March','Q1',2024,false),
(20240401,'2024-04-01','Monday',1,4,'April','Q2',2024,false);

INSERT INTO dim_product (product_id, product_name, category, subcategory, unit_price) VALUES
('P001','Samsung Galaxy S21','Electronics','Mobile',45999),
('P007','HP Laptop','Electronics','Laptop',52999),
('P002','Nike Running Shoes','Fashion','Footwear',3499);

INSERT INTO dim_customer (customer_id, customer_name, city, state, customer_segment) VALUES
('C001','Rahul Sharma','Bangalore','Karnataka','Consumer'),
('C002','Priya Patel','Mumbai','Maharashtra','Consumer'),
('C003','Amit Kumar','Delhi','Delhi','Corporate');

INSERT INTO fact_sales (date_key, product_key, customer_key, quantity_sold, unit_price, total_amount) VALUES
(20240115,1,1,1,45999,45999),
(20240201,2,2,1,52999,52999),
(20240301,3,3,2,3499,6998);
