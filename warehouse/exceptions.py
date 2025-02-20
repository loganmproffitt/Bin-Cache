
class StackFullError(Exception):
    """Raised when trying to add a bin to a full stack."""
    pass

class StackEmptyError(Exception):
    """Raised when trying to retrieve from an empty stack."""
    pass

class BinFullError(Exception):
    """Raised when trying to add an item to a full bin."""
    pass

class BinEmptyError(Exception):
    """Raised when trying to remove an item from an empty bin."""
    pass

class ItemNotFoundError(Exception):
    """Raised item is not found in a bin."""
    pass
