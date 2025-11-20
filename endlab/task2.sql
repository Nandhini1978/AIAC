
# --- AI-Designed Database Tables ---

# Table: authors
# Stores author information.
CREATE TABLE authors (
    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    biography TEXT
);

# Table: books
# Stores book details.
CREATE TABLE books (
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER NOT NULL,
    price REAL NOT NULL,
    stock INTEGER DEFAULT 0,
    FOREIGN KEY(author_id) REFERENCES authors(author_id)
);

# Table: sales
# Records sales transactions.
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    sale_date DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY(book_id) REFERENCES books(book_id)
);

-- ------------------------------------------------------------
-- 1. List best-selling books (by total quantity sold, descending)
-- ------------------------------------------------------------
SELECT
    b.book_id,
    b.title,
    a.name AS author_name,
    SUM(s.quantity) AS total_copies_sold
FROM
    books b
    JOIN authors a ON b.author_id = a.author_id
    LEFT JOIN sales s ON b.book_id = s.book_id
GROUP BY
    b.book_id, b.title, a.name
ORDER BY
    total_copies_sold DESC;

-- Test query: List top 3 best-selling books
SELECT
    b.book_id,
    b.title,
    a.name AS author_name,
    SUM(s.quantity) AS total_copies_sold
FROM
    books b
    JOIN authors a ON b.author_id = a.author_id
    LEFT JOIN sales s ON b.book_id = s.book_id
GROUP BY
    b.book_id, b.title, a.name
ORDER BY
    total_copies_sold DESC
LIMIT 3;

-- ------------------------------------------------------------
-- 2. Add a new author
-- ------------------------------------------------------------
INSERT INTO authors (name, biography) VALUES ('Jane Austen', 'English novelist known for works such as Pride and Prejudice.');

-- Test: Insert a new author without biography
INSERT INTO authors (name) VALUES ('Mark Twain');

-- ------------------------------------------------------------
-- 3. Update stock (e.g., Restock "book_id" 5 by 10 units)
-- ------------------------------------------------------------
UPDATE books
SET stock = stock + 10
WHERE book_id = 5;

-- Test: Reduce stock after a sale (book_id: 2, quantity sold: 4)
UPDATE books
SET stock = stock - 4
WHERE book_id = 2;


