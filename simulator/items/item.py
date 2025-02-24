import uuid
from datetime import datetime

class Item:
    """Represents a real-world instance of an item."""
    def __init__(self, item_type, entry_date=None):
        self.id = str(uuid.uuid4())
        self.item_type = item_type
        self.entry_date = entry_date if entry_date else datetime.now()

    def __repr__(self):
        return f"Item(id={self.id[:8]}, type={self.item_type.name}, entered={self.entry_date})"
