"""Domain exceptions for Quotations."""


class QuotationNotFound(Exception):
    """Raised when a Quotation record does not exist."""

    def __init__(self, item_id: int):
        super().__init__(f"Quotation {item_id} not found")
        self.item_id = item_id


class QuotationValidationError(ValueError):
    """Raised when Quotation data breaks a business rule."""
