CREATE TABLE IF NOT EXISTS order (
    id SERIAL PRIMARY KEY,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS item (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2) CHECK (price >= 0),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_item (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES order(id) ON DELETE CASCADE,
    item_id INT REFERENCES item(id) ON DELETE CASCADE,
    quantity INT CHECK (quantity > 0),
    price_at_purchase DECIMAL(10,2) check (price_at_purchase >= 0)
);

CREATE TABLE IF NOT EXISTS location (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS item_location (
    id SERIAL PRIMARY KEY,
    item_id INT REFERENCES item(id) ON DELETE CASCADE,
    location_id INT REFERENCES location(id) ON DELETE CASCADE,
    stock_quantity INT CHECK (stock_quantity >= 0) DEFAULT 0,
    last_updated TIMESTAMP DEFAULT NOW()
);