"""Service-layer tests for Welding Records."""
import pytest

from app.welding_records import service
from app.welding_records.exceptions import WeldingRecordNotFound, WeldingRecordValidationError
from app.welding_records.schemas import WeldingRecordCreate, WeldingRecordUpdate

PAYLOAD = {
    "job_order_id": 1,
    "welder_id": 1,
    "wps_number": "Sample wps number",
    "joint_id": "Sample joint id",
    "passed": True,
}


def test_create_and_get(db):
    created = service.create_item(db, WeldingRecordCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, WeldingRecordCreate(**PAYLOAD))
    service.create_item(db, WeldingRecordCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, WeldingRecordCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, WeldingRecordUpdate(wps_number="Updated value"))
    assert updated.wps_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, WeldingRecordCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(WeldingRecordNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(WeldingRecordValidationError):
        service.create_item(db, WeldingRecordCreate(**{**PAYLOAD, "wps_number": "   "}))
