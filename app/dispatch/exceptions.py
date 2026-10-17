"""Domain exceptions for Dispatch."""


class DispatchNotFound(Exception):
    """Raised when a Dispatch record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Dispatch {item_id} not found")
        self.item_id = item_id


class DispatchValidationError(ValueError):
    """Raised when Dispatch data breaks a business rule."""
