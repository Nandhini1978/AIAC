-- Retail Store Inventory system (MySQL)
-- File: mySQL_local3.session.sql

DROP TABLE IF EXISTS sales;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;

CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
) ENGINE=InnoDB;

CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    category_id INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    sku VARCHAR(50),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
        ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB;

CREATE TABLE sales (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    sale_price DECIMAL(10,2) NOT NULL, -- price per unit at time of sale
    sale_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    INDEX (sale_date)
) ENGINE=InnoDB;

-- Insert sample categories
INSERT INTO categories (name, description) VALUES
('Electronics', 'Phones, laptops, accessories'),
('Apparel', 'Clothing and accessories'),
('Groceries', 'Food and household items');

select * from categories;

-- Insert sample products
INSERT INTO products (name, category_id, unit_price, stock, sku) VALUES
('Smartphone X1', 1, 699.00, 50, 'ELEC-SMX1'),
('Laptop Pro 14', 1, 1299.00, 20, 'ELEC-LP14'),
('Wireless Headphones', 1, 149.99, 100, 'ELEC-WH01'),
('T-Shirt - Blue', 2, 19.99, 200, 'APP-TS-BL'),
('Jeans Regular', 2, 49.99, 150, 'APP-JE-01'),
('Organic Milk 1L', 3, 2.99, 300, 'GRO-MILK1'),
('Coffee Beans 500g', 3, 9.99, 120, 'GRO-CF500');

select * from products;
-- Insert sample sales (some sold at discounts / different prices)
INSERT INTO sales (product_id, quantity, sale_price, sale_date) VALUES
(1, 3, 699.00, '2025-10-01 10:15:00'),
(2, 1, 1199.00, '2025-10-02 12:30:00'), -- discounted laptop
(3, 10, 129.99, '2025-10-02 14:00:00'),
(4, 5, 19.99, '2025-10-03 09:20:00'),
(5, 2, 44.99, '2025-10-03 11:10:00'), -- promo price
(6, 20, 2.99, '2025-10-04 08:00:00'),
(7, 7, 9.49, '2025-10-04 09:00:00'), -- slight discount
(1, 1, 699.00, '2025-10-05 16:40:00'),
(3, 4, 149.99, '2025-10-05 17:20:00');

select * from sales;

-- Query: total sales (revenue) per category
SELECT
    c.category_id,
    c.name AS category,
    COALESCE(SUM(s.quantity * s.sale_price), 0) AS total_revenue,
    COALESCE(SUM(s.quantity), 0) AS total_units_sold
FROM categories c
LEFT JOIN products p ON p.category_id = c.category_id
LEFT JOIN sales s ON s.product_id = p.product_id
GROUP BY c.category_id, c.name
ORDER BY total_revenue DESC;