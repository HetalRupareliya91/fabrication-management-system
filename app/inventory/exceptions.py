"""Domain exceptions for Inventory."""


class InventoryItemNotFound(Exception):
    """Raised when a InventoryItem record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"InventoryItem {item_id} not found")
        self.item_id = item_id


class InventoryItemValidationError(ValueError):
    """Raised when InventoryItem data breaks a business rule."""
