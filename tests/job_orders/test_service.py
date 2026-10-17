"""Service-layer tests for Job Orders."""
import pytest

from app.job_orders import service
from app.job_orders.exceptions import JobOrderNotFound, JobOrderValidationError
from app.job_orders.schemas import JobOrderCreate, JobOrderUpdate

PAYLOAD = {
    "job_number": "Sample job number",
    "sales_order_id": 1,
    "part_number": "Sample part number",
    "quantity": 1,
    "status": "Sample status",
}


def test_create_and_get(db):
    created = service.create_item(db, JobOrderCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, JobOrderCreate(**PAYLOAD))
    service.create_item(db, JobOrderCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, JobOrderCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, JobOrderUpdate(job_number="Updated value"))
    assert updated.job_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, JobOrderCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(JobOrderNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(JobOrderValidationError):
        service.create_item(db, JobOrderCreate(**{**PAYLOAD, "job_number": "   "}))
