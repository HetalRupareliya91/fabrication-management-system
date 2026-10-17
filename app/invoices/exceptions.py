"""Domain exceptions for Invoices."""


class InvoiceNotFound(Exception):
    """Raised when a Invoice record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Invoice {item_id} not found")
        self.item_id = item_id


class InvoiceValidationError(ValueError):
    """Raised when Invoice data breaks a business rule."""
