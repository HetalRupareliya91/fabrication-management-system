"""Service-layer tests for Quality Checks."""
import pytest

from app.quality_checks import service
from app.quality_checks.exceptions import QualityCheckNotFound, QualityCheckValidationError
from app.quality_checks.schemas import QualityCheckCreate, QualityCheckUpdate

PAYLOAD = {
    "job_order_id": 1,
    "stage": "Sample stage",
    "inspector": "Sample inspector",
    "result": "Sample result",
    "check_date": "2026-01-15",
}


def test_create_and_get(db):
    created = service.create_item(db, QualityCheckCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, QualityCheckCreate(**PAYLOAD))
    service.create_item(db, QualityCheckCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, QualityCheckCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, QualityCheckUpdate(stage="Updated value"))
    assert updated.stage == "Updated value"


def test_delete(db):
    created = service.create_item(db, QualityCheckCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(QualityCheckNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(QualityCheckValidationError):
        service.create_item(db, QualityCheckCreate(**{**PAYLOAD, "stage": "   "}))
