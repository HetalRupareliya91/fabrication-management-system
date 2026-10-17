"""Service-layer tests for Operators."""
import pytest

from app.operators import service
from app.operators.exceptions import OperatorNotFound, OperatorValidationError
from app.operators.schemas import OperatorCreate, OperatorUpdate

PAYLOAD = {
    "employee_code": "Sample employee code",
    "name": "Sample name",
    "skill": "Sample skill",
    "certification": "Sample certification",
    "is_active": True,
}


def test_create_and_get(db):
    created = service.create_item(db, OperatorCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, OperatorCreate(**PAYLOAD))
    service.create_item(db, OperatorCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, OperatorCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, OperatorUpdate(employee_code="Updated value"))
    assert updated.employee_code == "Updated value"


def test_delete(db):
    created = service.create_item(db, OperatorCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(OperatorNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(OperatorValidationError):
        service.create_item(db, OperatorCreate(**{**PAYLOAD, "employee_code": "   "}))
