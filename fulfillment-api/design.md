Goal: Simulate a large scale fulfillment software with .Net and Postgres

Requirements:
- Order intake
    - Receive new orders and validate order info
    - Interact with order site or other places
- Order tracking
    - Moniter status (pending, processing, in transit, delivered, canceled, etc..)
    - Provide real time updates on status changes
- Analytics
    - Extract key data for performance and dashboard
- Inventory
    - Track inventory levels
- Manage exceptions

Structure
- We have inventory (what we have) and orders (what we need to send), and the two interact.
- For now, let's keep both in the same database for transactional consistency.
- Locations are likely complicated - for now let's just create Location and LocationOrder tables for prototyping

Database brainstorming
- We want to track orders and their status - Order table with status and other information such as location, etc.
    Order
        id
        created_at
        status
        updated_at
- We need to track items in orders and the inventory for each. So we want an Item table (tracking inventory and item type), and OrderItem (the instance and order it belongs to)
    Item
        id
        name
        description
        price
        created_at
        
    OrderItem
        id // allows more flexibility with partial orders, modifications, etc.
        order_id
        item_id
        quantity
        price_at_purchase
