CREATE TABLE customers (
  id INTEGER PRIMARY KEY,
  email VARCHAR(255)
);

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  total DECIMAL(10,2),
  FOREIGN KEY (customer_id) REFERENCES customers(id)
);
