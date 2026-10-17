"""Business validation rules for Maintenance."""
from .exceptions import MaintenanceTaskValidationError

STRING_FIELDS = ("maintenance_type", "remarks", )
NUMERIC_FIELDS = ("machine_id", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise MaintenanceTaskValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise MaintenanceTaskValidationError(f"{field} must not be negative")
    return cleaned
