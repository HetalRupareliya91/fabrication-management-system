"""Service-layer tests for Cutting Plans."""
import pytest

from app.cutting_plans import service
from app.cutting_plans.exceptions import CuttingPlanNotFound, CuttingPlanValidationError
from app.cutting_plans.schemas import CuttingPlanCreate, CuttingPlanUpdate

PAYLOAD = {
    "plan_number": "Sample plan number",
    "job_order_id": 1,
    "sheet_size": "Sample sheet size",
    "utilization_percent": 10.5,
    "status": "Sample status",
}


def test_create_and_get(db):
    created = service.create_item(db, CuttingPlanCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, CuttingPlanCreate(**PAYLOAD))
    service.create_item(db, CuttingPlanCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, CuttingPlanCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, CuttingPlanUpdate(plan_number="Updated value"))
    assert updated.plan_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, CuttingPlanCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(CuttingPlanNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(CuttingPlanValidationError):
        service.create_item(db, CuttingPlanCreate(**{**PAYLOAD, "plan_number": "   "}))
