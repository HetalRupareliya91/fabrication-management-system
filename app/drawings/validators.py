"""Business validation rules for Drawings."""
from .exceptions import DrawingValidationError

STRING_FIELDS = ("drawing_number", "revision", "title", )
NUMERIC_FIELDS = ("customer_id", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise DrawingValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise DrawingValidationError(f"{field} must not be negative")
    return cleaned
