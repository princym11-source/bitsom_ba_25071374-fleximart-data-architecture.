Section A: Limitations of RDBMS

Relational databases work best when data follows a fixed structure. In an e-commerce system where products have different attributes, such as electronics having specifications and clothing having sizes and colors, relational tables become difficult to manage. Adding new product attributes requires altering table schemas, which is time-consuming and risky in production systems. Storing customer reviews is also challenging because reviews must be split across multiple tables, increasing the number of joins and reducing query performance.

Section B: NoSQL Benefits

MongoDB addresses these challenges by using a flexible document-based schema. Each product can store different attributes without affecting other documents. Customer reviews can be embedded directly inside product documents, making data retrieval faster and simpler. MongoDB also supports horizontal scalability, allowing the product catalog to grow without performance bottlenecks.

Section C: Trade-offs

MongoDB does not provide the same level of transactional consistency as relational databases. Complex analytical queries and joins are more efficient in SQL-based systems compared to document databases.
