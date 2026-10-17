"""Business validation rules for Welding Records."""
from .exceptions import WeldingRecordValidationError

STRING_FIELDS = ("wps_number", "joint_id", )
NUMERIC_FIELDS = ("job_order_id", "welder_id", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise WeldingRecordValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise WeldingRecordValidationError(f"{field} must not be negative")
    return cleaned
