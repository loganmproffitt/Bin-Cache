CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_tracking (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE SET NULL,
    status VARCHAR(50) NOT NULL,
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    price DECIMAL(10,2) CHECK (price >= 0),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE RESTRICT,
    item_id INT REFERENCES items(id) ON DELETE RESTRICT,
    quantity INT CHECK (quantity > 0),
    price_at_purchase DECIMAL(10,2) check (price_at_purchase >= 0)
);

/* Create locations and link each item's inventory to a location. Also link orders to locations. */

CREATE TABLE IF NOT EXISTS locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS order_locations (
    order_id INT REFERENCES orders(id) ON DELETE RESTRICT,
    location_id INT REFERENCES locations(id) ON DELETE RESTRICT,
    PRIMARY KEY (order_id, location_id)
);

CREATE TABLE IF NOT EXISTS item_locations (
    item_id INT REFERENCES items(id) ON DELETE RESTRICT,
    location_id INT REFERENCES locations(id) ON DELETE RESTRICT,
    stock_quantity INT CHECK (stock_quantity >= 0) DEFAULT 0,
    last_updated TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY (item_id, location_id)
);

/* Exceptions table, stores info like issue_type and resolution dates */

CREATE TABLE IF NOT EXISTS order_exceptions (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    issue_type VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    status VARCHAR(50) DEFAULT 'open',
    created_at TIMESTAMP DEFAULT NOW(),
    resolved_at TIMESTAMP
);

/* Batching tables - table defining individual batches, then another linking orders to batches */

CREATE TABLE IF NOT EXISTS batches (
    id SERIAL PRIMARY KEY, 
    created_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50) DEFAULT 'pending'
);

CREATE TABLE IF NOT EXISTS order_batches (
    order_id INT REFERENCES orders(id) ON DELETE SET NULL,
    batch_id INT REFERENCES batches(id) ON DELETE SET NULL,
    PRIMARY KEY (order_id, batch_id)
);

/* Wave tables - Wave table and Batch-Wave junction table */

CREATE TABLE IF NOT EXISTS waves (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT NOW(),
    status VARCHAR(50) DEFAULT 'pending',
    wave_type VARCHAR(50),
    estimated_completion TIMESTAMP,
    completed_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS batch_waves (
    batch_id INT REFERENCES batches(id) ON DELETE RESTRICT,
    wave_id INT REFERENCES waves(id) ON DELETE RESTRICT,
    PRIMARY KEY (batch_id, wave_id)
);