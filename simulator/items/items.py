from items.item_type import ItemType
from items.item import Item

class Basketball(ItemType):
    def __init__(self):
        super().__init__("Basketball", "Sports")

class Baseball(ItemType):
    def __init__(self):
        super().__init__("Baseball", "Sports")

class Soap(ItemType):
    def __init__(self):
        super().__init__("Soap", "Hygeine")

class Toothbrush(ItemType):
    def __init__(self):
        super().__init__("Toothbrush", "Hygeine")

class Laptop(ItemType):
    def __init__(self):
        super().__init__("Laptop", "Technology")

class GPU(ItemType):
    def __init__(self):
        super().__init__("GPU", "Technology")
