CREATE TABLE meesho_sales_products(

   Product_ID VARCHAR(10),
   Product_Name TEXT,
   Category TEXT,
   Sub_Category TEXT,
   Price INT,
   Discount_Price INT,
   Ratings NUMERIC(3,2),
   Reviews INT,
   Seller_Name TEXT,
   Delivery_Time VARCHAR(20),
   Availability VARCHAR(20)
);

SELECT * FROM meesho_sales_products;

COPY meesho_sales_products(Product_ID,Product_Name,Category,Sub_Category,Price,Discount_Price,Ratings,Reviews,
Seller_Name,Delivery_Time,Availability)
FROM 'C:\Program Files\PostgreSQL\17\data\meesho_product_dataset_india.csv'
CSV HEADER;


-- ---- SQL QUERIES -------
-- 1.	View all products

SELECT * FROM meesho_sales_products;

-- 2.	Total number of products
SELECT COUNT(*) AS Total_Products
FROM meesho_sales_products;

-- 3.	List unique product categories
SELECT DISTINCT Category
FROM meesho_sales_products;

-- 4.	Count of products per category
SELECT Category,COUNT(*) AS Product_Count
FROM meesho_sales_products
GROUP BY Category;

-- 5.	Average price by category

SELECT Category,AVG(Price)AS Average_Price
FROM meesho_sales_products
GROUP BY Category;


-- 6.Top 5 most expensive products (Original Price)

SELECT Product_Name,Price
FROM meesho_sales_products
ORDER BY Price DESC
LIMIT 5;

-- 7.Products with rating above 4.0

SELECT Product_Name,Ratings
FROM meesho_sales_products
WHERE Ratings > 4.0;

-- 8.Top 5 products with highest number of reviews

SELECT Product_Name,Reviews
FROM meesho_sales_products
ORDER BY Reviews DESC
LIMIT 5;

-- 9.Products currently out of stock
SELECT Product_Name
FROM meesho_sales_products
WHERE Availability = 'Out-of-Stock';
-- WHERE Availability = 'In-Stock';

--10. Seller-wise product count
SELECT Seller_Name,COUNT(*) AS Total_Product
FROM meesho_sales_products
GROUP BY Seller_Name;

-- ---------- END OF QUERIES -----------------
