import uuid
from datetime import datetime
from warehouse.exceptions import BinFullError, BinEmptyError, ItemNotFoundError

class Bin:
    def __init__(self, max_items=5):
        self.items = []
        self.id = str(uuid.uuid4())
        self.entry_date = datetime.now()
        self.max_items = max_items

    def add_item(self, item):
        if self.is_full():
            raise BinFullError(f"Cannot add to bin with id {self.id[:8]}")
        self.items.append(item)
    
    def remove_item(self, item_id):
        if self.is_empty():
            raise BinEmptyError(f"Can't remove item; bin {self.id[:8]} is empty.")
        for i, item in enumerate(self.items):
            if item.id == item_id:
                return self.items.pop(i) 
        raise ItemNotFoundError(f"Item {item_id[:8]} not found in bin {self.id[:8]}")

    def get_item_count(self):
        return len(self.items)
    
    def __repr__(self):
        item_details = ", ".join(f"{item.item_type.name}({item.id[:8]})" for item in self.items)
        return f"Bin(id={self.id[:8]}, items=[{item_details}])"

    def is_full(self):
        return len(self.items) >= self.max_items
    
    def is_empty(self):
        return len(self.items) == 0