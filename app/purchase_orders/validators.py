"""Business validation rules for Purchase Orders."""
from .exceptions import PurchaseOrderValidationError

STRING_FIELDS = ("po_number", "status", )
NUMERIC_FIELDS = ("supplier_id", "total_amount", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise PurchaseOrderValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise PurchaseOrderValidationError(f"{field} must not be negative")
    return cleaned
