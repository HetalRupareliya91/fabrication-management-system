"""Domain exceptions for Drawings."""


class DrawingNotFound(Exception):
    """Raised when a Drawing record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Drawing {item_id} not found")
        self.item_id = item_id


class DrawingValidationError(ValueError):
    """Raised when Drawing data breaks a business rule."""
