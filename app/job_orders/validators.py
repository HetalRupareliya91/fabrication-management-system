"""Business validation rules for Job Orders."""
from .exceptions import JobOrderValidationError

STRING_FIELDS = ("job_number", "part_number", "status", )
NUMERIC_FIELDS = ("sales_order_id", "quantity", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise JobOrderValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise JobOrderValidationError(f"{field} must not be negative")
    return cleaned
