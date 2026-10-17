"""Domain exceptions for Customers."""


class CustomerNotFound(Exception):
    """Raised when a Customer record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Customer {item_id} not found")
        self.item_id = item_id


class CustomerValidationError(ValueError):
    """Raised when Customer data breaks a business rule."""
