"""Business validation rules for Painting."""
from .exceptions import PaintingRecordValidationError

STRING_FIELDS = ("paint_system", )
NUMERIC_FIELDS = ("job_order_id", "dft_microns", "coats", )


def validate(data: dict) -> dict:
    """Reject blank text and negative quantities. Returns cleaned data."""
    cleaned = dict(data)
    for field in STRING_FIELDS:
        value = cleaned.get(field)
        if value is not None:
            if not str(value).strip():
                raise PaintingRecordValidationError(f"{field} must not be blank")
            cleaned[field] = str(value).strip()
    for field in NUMERIC_FIELDS:
        value = cleaned.get(field)
        if value is not None and value < 0:
            raise PaintingRecordValidationError(f"{field} must not be negative")
    return cleaned
