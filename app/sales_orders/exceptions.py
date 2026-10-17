"""Domain exceptions for Sales Orders."""


class SalesOrderNotFound(Exception):
    """Raised when a SalesOrder record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"SalesOrder {item_id} not found")
        self.item_id = item_id


class SalesOrderValidationError(ValueError):
    """Raised when SalesOrder data breaks a business rule."""
