"""Domain exceptions for Quality Checks."""


class QualityCheckNotFound(Exception):
    """Raised when a QualityCheck record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"QualityCheck {item_id} not found")
        self.item_id = item_id


class QualityCheckValidationError(ValueError):
    """Raised when QualityCheck data breaks a business rule."""
