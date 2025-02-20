from items.item import Item

class ItemType:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def create_item(self, **kwargs):
        return Item(self, **kwargs)
    
    def __repr__(self):
        return f"ItemType(name={self.name}, category={self.category})"