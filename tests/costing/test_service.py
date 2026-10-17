"""Service-layer tests for Job Costing."""
import pytest

from app.costing import service
from app.costing.exceptions import JobCostNotFound, JobCostValidationError
from app.costing.schemas import JobCostCreate, JobCostUpdate

PAYLOAD = {
    "job_order_id": 1,
    "currency": "Sample currency",
    "material_cost": 10.5,
    "labour_cost": 10.5,
    "total_cost": 10.5,
}


def test_create_and_get(db):
    created = service.create_item(db, JobCostCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, JobCostCreate(**PAYLOAD))
    service.create_item(db, JobCostCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, JobCostCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, JobCostUpdate(currency="Updated value"))
    assert updated.currency == "Updated value"


def test_delete(db):
    created = service.create_item(db, JobCostCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(JobCostNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(JobCostValidationError):
        service.create_item(db, JobCostCreate(**{**PAYLOAD, "currency": "   "}))
