"""Business validation rules for Inventory."""
from .exceptions import InventoryItemValidationError

STRING_FIELDS = ("material_code", "location", "batch_no", )
NUMERIC_FIELDS = ("quantity", "reorder_level", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise InventoryItemValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise InventoryItemValidationError(f"{field} must not be negative")
    return cleaned
