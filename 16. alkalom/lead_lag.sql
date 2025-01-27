/*
 * lead()
 * lag()
 * 
 * */

-- Teszt tábla létrehozása
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    sale_date DATE,
    sale_amount NUMERIC(10,2)
);

-- Adatok beszúrása
INSERT INTO sales (customer_name, sale_date, sale_amount) VALUES
('John Doe', '2024-01-01', 100.00),
('Jane Smith', '2024-01-03', 150.00),
('John Doe', '2024-01-05', 200.00),
('Alice Johnson', '2024-01-07', 250.00),
('John Doe', '2024-01-10', 300.00),
('Jane Smith', '2024-01-12', 180.00),
('Alice Johnson', '2024-01-15', 400.00),
('John Doe', '2024-01-18', 500.00);


SELECT 
lag(sale_amount, 1)over(partition by s.customer_name order by sale_date asc) as prev_sale_amount,
lead(sale_amount, 1)over(partition by s.customer_name order by sale_date asc) - sale_amount as next_sale_amount,
s.*
FROM sales s;
 
