"""Domain exceptions for Painting."""


class PaintingRecordNotFound(Exception):
    """Raised when a PaintingRecord record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"PaintingRecord {item_id} not found")
        self.item_id = item_id


class PaintingRecordValidationError(ValueError):
    """Raised when PaintingRecord data breaks a business rule."""
