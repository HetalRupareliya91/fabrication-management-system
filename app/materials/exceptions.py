"""Domain exceptions for Materials."""


class MaterialNotFound(Exception):
    """Raised when a Material record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Material {item_id} not found")
        self.item_id = item_id


class MaterialValidationError(ValueError):
    """Raised when Material data breaks a business rule."""
