"""Service-layer tests for Users."""
import pytest

from app.users import service
from app.users.exceptions import UserNotFound, UserValidationError
from app.users.schemas import UserCreate, UserUpdate

PAYLOAD = {
    "username": "Sample username",
    "email": "Sample email",
    "full_name": "Sample full name",
    "role": "Sample role",
    "is_active": True,
}


def test_create_and_get(db):
    created = service.create_item(db, UserCreate(**PAYLOAD))
    assert created.id is not None
    assert service.get_item(db, created.id).id == created.id


def test_list_returns_created_items(db):
    service.create_item(db, UserCreate(**PAYLOAD))
    service.create_item(db, UserCreate(**PAYLOAD))
    assert len(service.list_items(db)) == 2


def test_update(db):
    created = service.create_item(db, UserCreate(**PAYLOAD))
    updated = service.update_item(db, created.id, UserUpdate(username="Updated value"))
    assert updated.username == "Updated value"


def test_delete(db):
    created = service.create_item(db, UserCreate(**PAYLOAD))
    service.delete_item(db, created.id)
    with pytest.raises(UserNotFound):
        service.get_item(db, created.id)


def test_blank_text_is_rejected(db):
    with pytest.raises(UserValidationError):
        service.create_item(db, UserCreate(**{**PAYLOAD, "username": "   "}))
