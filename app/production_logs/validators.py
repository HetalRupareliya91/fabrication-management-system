"""Business validation rules for Production Logs."""
from .exceptions import ProductionLogValidationError

STRING_FIELDS = ("remarks", )
NUMERIC_FIELDS = ("job_order_id", "operator_id", "quantity_done", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise ProductionLogValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise ProductionLogValidationError(f"{field} must not be negative")
    return cleaned
