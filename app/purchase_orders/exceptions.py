"""Domain exceptions for Purchase Orders."""


class PurchaseOrderNotFound(Exception):
    """Raised when a PurchaseOrder record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"PurchaseOrder {item_id} not found")
        self.item_id = item_id


class PurchaseOrderValidationError(ValueError):
    """Raised when PurchaseOrder data breaks a business rule."""
