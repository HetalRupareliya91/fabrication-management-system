"""Business validation rules for Work Centers."""
from .exceptions import WorkCenterValidationError

STRING_FIELDS = ("code", "name", )
NUMERIC_FIELDS = ("capacity_hours", "cost_per_hour", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise WorkCenterValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise WorkCenterValidationError(f"{field} must not be negative")
    return cleaned
