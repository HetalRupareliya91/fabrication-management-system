"""Service-layer tests for Purchase Orders."""
import pytest

from app.purchase_orders import service
from app.purchase_orders.exceptions import PurchaseOrderNotFound, PurchaseOrderValidationError
from app.purchase_orders.schemas import PurchaseOrderCreate, PurchaseOrderUpdate

PAYLOAD = {
    "po_number": "Sample po number",
    "supplier_id": 1,
    "order_date": "2026-01-15",
    "total_amount": 10.5,
    "status": "Sample status",
}


def test_create_and_get(db):
    created = service.create_item(db, PurchaseOrderCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, PurchaseOrderCreate(**PAYLOAD))
    service.create_item(db, PurchaseOrderCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, PurchaseOrderCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, PurchaseOrderUpdate(po_number="Updated value"))
    assert updated.po_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, PurchaseOrderCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(PurchaseOrderNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(PurchaseOrderValidationError):
        service.create_item(db, PurchaseOrderCreate(**{**PAYLOAD, "po_number": "   "}))
