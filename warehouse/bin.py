import uuid
from datetime import datetime

class Bin:
    def __init__(self):
        self.items = []
        self.id = str(uuid.uuid4())
        self.entry_date = datetime.now()

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item_id):
        print("remove item")

    def get_item_count(self):
        return len(self.items)
    
    def __repr__(self):
        item_details = ", ".join(f"{item.item_type.name}({item.id[:8]})" for item in self.items)
        return f"Bin(id={self.id[:8]}, items=[{item_details}])"
