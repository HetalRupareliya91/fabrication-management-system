"""Domain exceptions for Non-Conformance Reports."""


class NonConformanceNotFound(Exception):
    """Raised when a NonConformance record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"NonConformance {item_id} not found")
        self.item_id = item_id


class NonConformanceValidationError(ValueError):
    """Raised when NonConformance data breaks a business rule."""
