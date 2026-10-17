"""Business validation rules for Users."""
from .exceptions import UserValidationError

STRING_FIELDS = ("username", "email", "full_name", "role", )
NUMERIC_FIELDS = ()


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise UserValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise UserValidationError(f"{field} must not be negative")
    return cleaned
