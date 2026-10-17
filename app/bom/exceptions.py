"""Domain exceptions for Bill of Materials."""


class BomLineNotFound(Exception):
    """Raised when a BomLine record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"BomLine {item_id} not found")
        self.item_id = item_id


class BomLineValidationError(ValueError):
    """Raised when BomLine data breaks a business rule."""
