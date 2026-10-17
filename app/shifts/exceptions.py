"""Domain exceptions for Shifts."""


class ShiftNotFound(Exception):
    """Raised when a Shift record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Shift {item_id} not found")
        self.item_id = item_id


class ShiftValidationError(ValueError):
    """Raised when Shift data breaks a business rule."""
