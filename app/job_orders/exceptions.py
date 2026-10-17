"""Domain exceptions for Job Orders."""


class JobOrderNotFound(Exception):
    """Raised when a JobOrder record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"JobOrder {item_id} not found")
        self.item_id = item_id


class JobOrderValidationError(ValueError):
    """Raised when JobOrder data breaks a business rule."""
