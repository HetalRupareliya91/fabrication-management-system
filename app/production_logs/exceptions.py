"""Domain exceptions for Production Logs."""


class ProductionLogNotFound(Exception):
    """Raised when a ProductionLog record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"ProductionLog {item_id} not found")
        self.item_id = item_id


class ProductionLogValidationError(ValueError):
    """Raised when ProductionLog data breaks a business rule."""
