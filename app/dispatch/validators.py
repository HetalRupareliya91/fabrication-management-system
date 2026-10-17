"""Business validation rules for Dispatch."""
from .exceptions import DispatchValidationError

STRING_FIELDS = ("dispatch_number", "vehicle_number", )
NUMERIC_FIELDS = ("sales_order_id", "weight_kg", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise DispatchValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise DispatchValidationError(f"{field} must not be negative")
    return cleaned
