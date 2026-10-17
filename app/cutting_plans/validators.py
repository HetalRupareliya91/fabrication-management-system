"""Business validation rules for Cutting Plans."""
from .exceptions import CuttingPlanValidationError

STRING_FIELDS = ("plan_number", "sheet_size", "status", )
NUMERIC_FIELDS = ("job_order_id", "utilization_percent", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise CuttingPlanValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise CuttingPlanValidationError(f"{field} must not be negative")
    return cleaned
