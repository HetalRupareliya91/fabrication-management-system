"""Service-layer tests for Maintenance."""
import pytest

from app.maintenance import service
from app.maintenance.exceptions import MaintenanceTaskNotFound, MaintenanceTaskValidationError
from app.maintenance.schemas import MaintenanceTaskCreate, MaintenanceTaskUpdate

PAYLOAD = {
    "machine_id": 1,
    "maintenance_type": "Sample maintenance type",
    "scheduled_on": "2026-01-15",
    "completed": True,
    "remarks": "Sample remarks",
}


def test_create_and_get(db):
    created = service.create_item(db, MaintenanceTaskCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, MaintenanceTaskCreate(**PAYLOAD))
    service.create_item(db, MaintenanceTaskCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, MaintenanceTaskCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, MaintenanceTaskUpdate(maintenance_type="Updated value"))
    assert updated.maintenance_type == "Updated value"


def test_delete(db):
    created = service.create_item(db, MaintenanceTaskCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(MaintenanceTaskNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(MaintenanceTaskValidationError):
        service.create_item(db, MaintenanceTaskCreate(**{**PAYLOAD, "maintenance_type": "   "}))
