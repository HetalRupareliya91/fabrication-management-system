"""Business validation rules for Job Costing."""
from .exceptions import JobCostValidationError

STRING_FIELDS = ("currency", )
NUMERIC_FIELDS = ("job_order_id", "material_cost", "labour_cost", "total_cost", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise JobCostValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise JobCostValidationError(f"{field} must not be negative")
    return cleaned
