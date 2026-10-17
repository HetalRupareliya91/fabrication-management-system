"""Service-layer tests for Invoices."""
import pytest

from app.invoices import service
from app.invoices.exceptions import InvoiceNotFound, InvoiceValidationError
from app.invoices.schemas import InvoiceCreate, InvoiceUpdate

PAYLOAD = {
    "invoice_number": "Sample invoice number",
    "sales_order_id": 1,
    "invoice_date": "2026-01-15",
    "amount": 10.5,
    "paid": True,
}


def test_create_and_get(db):
    created = service.create_item(db, InvoiceCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, InvoiceCreate(**PAYLOAD))
    service.create_item(db, InvoiceCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, InvoiceCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, InvoiceUpdate(invoice_number="Updated value"))
    assert updated.invoice_number == "Updated value"


def test_delete(db):
    created = service.create_item(db, InvoiceCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(InvoiceNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(InvoiceValidationError):
        service.create_item(db, InvoiceCreate(**{**PAYLOAD, "invoice_number": "   "}))
