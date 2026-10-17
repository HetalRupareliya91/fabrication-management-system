"""Domain exceptions for Suppliers."""


class SupplierNotFound(Exception):
    """Raised when a Supplier record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Supplier {item_id} not found")
        self.item_id = item_id


class SupplierValidationError(ValueError):
    """Raised when Supplier data breaks a business rule."""
