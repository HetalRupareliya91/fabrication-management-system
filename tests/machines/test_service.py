"""Service-layer tests for Machines."""
import pytest

from app.machines import service
from app.machines.exceptions import MachineNotFound, MachineValidationError
from app.machines.schemas import MachineCreate, MachineUpdate

PAYLOAD = {
    "machine_code": "Sample machine code",
    "name": "Sample name",
    "work_center_id": 1,
    "make": "Sample make",
    "commissioned_on": "2026-01-15",
}


def test_create_and_get(db):
    created = service.create_item(db, MachineCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, MachineCreate(**PAYLOAD))
    service.create_item(db, MachineCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, MachineCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, MachineUpdate(machine_code="Updated value"))
    assert updated.machine_code == "Updated value"


def test_delete(db):
    created = service.create_item(db, MachineCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(MachineNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(MachineValidationError):
        service.create_item(db, MachineCreate(**{**PAYLOAD, "machine_code": "   "}))
