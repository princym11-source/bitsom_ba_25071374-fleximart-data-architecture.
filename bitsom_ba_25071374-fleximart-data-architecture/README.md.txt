# FlexiMart Data Architecture Project

**Course:** Data for Artificial Intelligence  
**Module:** AI Data Architecture Design and Implementation  

**Student Name:** Princy Mishra  
**Student ID:**  [bitsom_ba_25071374]
**Email:** [princymishra116@gmail.com]  

---

## 📌 Project Overview

This project demonstrates the complete design and implementation of a modern data architecture solution for **FlexiMart**, a fictional e-commerce company.  
The work covers the entire data lifecycle — from raw CSV ingestion and cleaning, to relational database design, NoSQL analysis, and finally a dimensional data warehouse built for analytics.

The objective of this assignment is to showcase practical data engineering skills including **ETL development**, **schema design**, **SQL analytics**, **NoSQL modeling**, and **OLAP reporting**.

---

## 🧱 Architecture Summary

The project is divided into three major layers:

1. **Operational Data Layer (OLTP)**
   - Raw CSV files
   - Cleaned and loaded into a relational database (MySQL)

2. **NoSQL Layer**
   - Product catalog modeled using MongoDB
   - Flexible schema with embedded documents

3. **Analytics Layer (OLAP)**
   - Star schema data warehouse
   - Analytical queries for business insights

---

## 📂 Repository Structure

bitsom_ba_25071374-fleximart-data-architecture/
│
├── data/
│ ├── customers_raw.csv
│ ├── products_raw.csv
│ └── sales_raw.csv
│
├── part1-database-etl/
│ ├── README.md
│ ├── etl_pipeline.py
│ ├── schema_documentation.md
│ ├── business_queries.sql
│ ├── data_quality_report.txt
│ └── requirements.txt
│
├── part2-nosql/
│ ├── README.md
│ ├── nosql_analysis.md
│ ├── mongodb_operations.js
│ └── products_catalog.json
│
├── part3-datawarehouse/
│ ├── README.md
│ ├── star_schema_design.md
│ ├── warehouse_schema.sql
│ ├── warehouse_data.sql
│ └── analytics_queries.sql
│
├── .gitignore
└── README.md


---

## ⚙️ Technologies Used

- **Programming Language:** Python 3.x  
- **Libraries:** pandas, mysql-connector-python  
- **Relational Database:** MySQL 8.0  
- **NoSQL Database:** MongoDB 6.0  
- **Query Languages:** SQL, MongoDB Aggregation Framework  

---

## 🚀 Setup & Execution Instructions

### 1️⃣ Database Setup (MySQL)

```bash
# Create required databases
mysql -u root -p -e "CREATE DATABASE fleximart;"
mysql -u root -p -e "CREATE DATABASE fleximart_dw;"

2️⃣ Run ETL Pipeline (Part 1)

pip install -r part1-database-etl/requirements.txt
python part1-database-etl/etl_pipeline.py

This will:
-- Read raw CSV files
-- Clean and standardize data
-- Load data into MySQL tables
--Generate data_quality_report.txt

3️⃣ Execute Business Queries
mysql -u root -p fleximart < part1-database-etl/business_queries.sql

4️⃣ MongoDB Operations (Part 2)
mongosh < part2-nosql/mongodb_operations.js

5️⃣ Data Warehouse Setup (Part 3)
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_schema.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/warehouse_data.sql
mysql -u root -p fleximart_dw < part3-datawarehouse/analytics_queries.sql

📊 Key Features Implemented
✔ ETL Pipeline

-- Duplicate removal
-- Missing value handling
-- Date and category standardization
-- Automated data quality reporting

✔ Relational Database Design

-- Fully normalized schema (3NF)
-- Referential integrity using foreign keys

✔ Business Analytics (SQL)

-- Customer purchase analysis
-- Product category performance
-- Monthly sales trends with cumulative revenue

✔ NoSQL Modeling

-- Flexible product schema
-- Embedded reviews
-- Aggregation-based analysis

✔ Data Warehouse & OLAP

-- Star schema implementation
-- Time-based drill-down analysis
-- Product and customer segmentation analytics

📘 Key Learnings

-- Designing robust ETL pipelines for imperfect real-world data
-- Choosing between relational and NoSQL databases based on use cases
-- Applying dimensional modeling concepts for analytics
-- Writing efficient SQL for both OLTP and OLAP systems

⚠️ Challenges Faced & Solutions

- Handling inconsistent source data
  -- Solved by implementing validation, standardization, and default handling in the ETL layer.

- Designing a scalable analytics model
  -- Solved by using a star schema with surrogate keys and proper granularity.

🧾 Submission Notes

-- All SQL scripts run without errors
-- Foreign key constraints are maintained
-- Code is commented and modular
-- Commit history follows assignment guidelines

📎 Author
-- Princy Mishra















