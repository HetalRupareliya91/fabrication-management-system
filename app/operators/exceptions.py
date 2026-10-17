"""Domain exceptions for Operators."""


class OperatorNotFound(Exception):
    """Raised when a Operator record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Operator {item_id} not found")
        self.item_id = item_id


class OperatorValidationError(ValueError):
    """Raised when Operator data breaks a business rule."""
