"""Service-layer tests for Production Logs."""
import pytest

from app.production_logs import service
from app.production_logs.exceptions import ProductionLogNotFound, ProductionLogValidationError
from app.production_logs.schemas import ProductionLogCreate, ProductionLogUpdate

PAYLOAD = {
    "job_order_id": 1,
    "operator_id": 1,
    "quantity_done": 1,
    "remarks": "Sample remarks",
    "log_date": "2026-01-15",
}


def test_create_and_get(db):
    created = service.create_item(db, ProductionLogCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, ProductionLogCreate(**PAYLOAD))
    service.create_item(db, ProductionLogCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, ProductionLogCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, ProductionLogUpdate(remarks="Updated value"))
    assert updated.remarks == "Updated value"


def test_delete(db):
    created = service.create_item(db, ProductionLogCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(ProductionLogNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(ProductionLogValidationError):
        service.create_item(db, ProductionLogCreate(**{**PAYLOAD, "remarks": "   "}))
