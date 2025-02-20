
class StackFullError(Exception):
    """Raised when trying to add a bin to a full stack."""
    pass

class StackEmptyError(Exception):
    """Raised when trying to retrieve from an empty stack."""
    pass
