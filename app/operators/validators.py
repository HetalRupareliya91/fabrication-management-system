"""Business validation rules for Operators."""
from .exceptions import OperatorValidationError

STRING_FIELDS = ("employee_code", "name", "skill", "certification", )
NUMERIC_FIELDS = ()


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise OperatorValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise OperatorValidationError(f"{field} must not be negative")
    return cleaned
