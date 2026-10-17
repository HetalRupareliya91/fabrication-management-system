"""Domain exceptions for Work Centers."""


class WorkCenterNotFound(Exception):
    """Raised when a WorkCenter record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"WorkCenter {item_id} not found")
        self.item_id = item_id


class WorkCenterValidationError(ValueError):
    """Raised when WorkCenter data breaks a business rule."""
