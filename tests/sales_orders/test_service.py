"""Service-layer tests for Sales Orders."""
import pytest

from app.sales_orders import service
from app.sales_orders.exceptions import SalesOrderNotFound, SalesOrderValidationError
from app.sales_orders.schemas import SalesOrderCreate, SalesOrderUpdate

PAYLOAD = {
    "so_number": "Sample so number",
    "customer_id": 1,
    "order_date": "2026-01-15",
    "delivery_date": "2026-01-15",
    "status": "Sample status",
}


def test_create_and_get(db):
    created = service.create_item(db, SalesOrderCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, SalesOrderCreate(**PAYLOAD))
    service.create_item(db, SalesOrderCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, SalesOrderCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, SalesOrderUpdate(so_number="Updated value"))
    assert updated.so_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, SalesOrderCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(SalesOrderNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(SalesOrderValidationError):
        service.create_item(db, SalesOrderCreate(**{**PAYLOAD, "so_number": "   "}))
