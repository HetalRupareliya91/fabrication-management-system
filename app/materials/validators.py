"""Business validation rules for Materials."""
from .exceptions import MaterialValidationError

STRING_FIELDS = ("code", "description", "grade", "unit", )
NUMERIC_FIELDS = ("thickness_mm", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise MaterialValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise MaterialValidationError(f"{field} must not be negative")
    return cleaned
