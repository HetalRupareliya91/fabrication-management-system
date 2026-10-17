"""Domain exceptions for Welding Records."""


class WeldingRecordNotFound(Exception):
    """Raised when a WeldingRecord record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"WeldingRecord {item_id} not found")
        self.item_id = item_id


class WeldingRecordValidationError(ValueError):
    """Raised when WeldingRecord data breaks a business rule."""
